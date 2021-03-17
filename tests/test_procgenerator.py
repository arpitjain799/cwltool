"""ProcessGenerator related tests."""

from typing import Any

from cwltool.main import main

from .util import get_data


def test_missing_enable_ext(monkeypatch: Any) -> None:
    """Test missing enable-ext option fails.

    Check that a workflow that needs `--enable-ext` and
    `--enable-dev` fails without those options and passes with them.
    """
    monkeypatch.delenv("CWLTOOL_OPTIONS", raising=False)
    assert main([get_data("tests/wf/generator/zing.cwl"), "--zing", "zipper"]) == 1

    assert (
        main(
            [
                "--enable-ext",
                "--enable-dev",
                get_data("tests/wf/generator/zing.cwl"),
                "--zing",
                "zipper",
            ]
        )
        == 0
    )

    monkeypatch.setenv("CWLTOOL_OPTIONS", "--enable-ext --enable-dev")
    assert main([get_data("tests/wf/generator/zing.cwl"), "--zing", "zipper"]) == 0
