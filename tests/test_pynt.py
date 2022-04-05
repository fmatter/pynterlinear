import pynterlinear


def test_gloss():
    test_cases = {
        "3P-kill-1SG": "\\gl{3}\\gl{p}-kill-\\gl{1}\\gl{sg}",
        "K. kill-REM": "K. kill-\\gl{rem}",
        # "laugh[3SG.IMP]": "laugh[\\gl{3}\\gl{sg}.\\gl{imp}]",
        "3>3-kill-IPFV.PST": "\\gl{3}>\\gl{3}-kill-\\gl{ipfv}.\\gl{pst}",
        "go-3SG.PST-1>2-CAUS[ERG]":
        "go-\\gl{3}\\gl{sg}.\\gl{pst}-\\gl{1}>\\gl{2}-\\gl{caus}[\\gl{erg}]",
        # "K.-ERG[3SG>2PL.PST]":
        # "K.-\\gl{erg}[\\gl{3}\\gl{sg}>\\gl{2}\\gl{pl}.\\gl{pst}]",
        "M.SG": "\\gl{m}.\\gl{sg}",
        "test-3.PROG and-more-words": "test-\\gl{3}.\\gl{prog} and-more-words",
        "child\\PL": "child\\textbackslash{}\\gl{pl}",
        "G14-child": "\\gl{g}14-child",
        "child(G14)": "child(\\gl{g}14)",
        "1>3": "\\gl{1}>\\gl{3}",
        "1S": "\\gl{1}\\gl{s}",
        "3SG.F": "\\gl{3}\\gl{sg}.\\gl{f}",
        "3>F": "\\gl{3}>\\gl{f}",
        "F>3": "\\gl{f}>\\gl{3}",
        "1SG.PRO": "\\gl{1}\\gl{sg}.\\gl{pro}",
    }
    for raw, expex in test_cases.items():
        assert pynterlinear.get_expex_code(raw) == expex
