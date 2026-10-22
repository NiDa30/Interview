#!/usr/bin/env python3
"""Regression tests for book QA. Runs locally without GitHub Actions."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import io
import json
from contextlib import redirect_stdout
import qa_book

class BookQaTests(unittest.TestCase):
    def run_case(self, content, extra_files=None):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            base=root/"book"/"chapters"/"chapter-01"
            base.mkdir(parents=True)
            (base/"01-01-sample.md").write_text(content,encoding="utf-8")
            for name, text in (extra_files or {}).items():
                target=root/name
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_text(text,encoding="utf-8")
            output=io.StringIO()
            with patch.object(qa_book,"ROOT",root),patch.object(qa_book,"CHAPTERS",root/"book"/"chapters"),redirect_stdout(output):
                code=qa_book.report()
            return code,json.loads(output.getvalue())

    def test_valid_mermaid_and_link(self):
        body="# Sample\n\n[Related](../chapter-02/02-01-next.md)\n\n"+'\x60'*3+"mermaid\nflowchart LR\n A --> B\n"+'\x60'*3+"\n面接官： Q\n応募者： A\n"
        code,res=self.run_case(body,{"book/chapters/chapter-02/02-01-next.md":"# Next"})
        self.assertEqual(code,0)
        self.assertEqual(res["mermaid_fences"],1)

    def test_missing_link_fails(self):
        code,res=self.run_case("# Test\n[Missing](missing.md)\n")
        self.assertNotEqual(code,0)
        self.assertIn("broken-relative-link",[x["rule"] for x in res["errors"]])

    def test_invalid_mermaid_header_fails(self):
        code,res=self.run_case("# Test\n"+'\x60'*3+"mermaid\nĐây là hướng dẫn\n"+'\x60'*3+"\n")
        self.assertNotEqual(code,0)
        self.assertIn("invalid-mermaid-header",[x["rule"] for x in res["errors"]])

    def test_unpaired_fence_fails(self):
        code,res=self.run_case("# Test\n"+'\x60'*3+"mermaid\nflowchart LR\n A --> B\n")
        self.assertNotEqual(code,0)
        self.assertIn("unpaired-fence",[x["rule"] for x in res["errors"]])

    def test_placeholder_is_warning_only(self):
        code,res=self.run_case("# Test\n面接官： Q\n応募者： 【実際の経験】\n")
        self.assertEqual(code,0)
        self.assertIn("personalization-needed",[x["rule"] for x in res["warnings"]])

if __name__=="__main__":
    unittest.main(verbosity=2)
