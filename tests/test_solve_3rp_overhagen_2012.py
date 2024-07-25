import logging
import webbrowser
from pathlib import Path

from pyroll.basic import Profile, PassSequence, ThreeRollPass, Roll, CircularOvalGroove, Transport, RoundGroove, \
    SwedishOvalGroove
from pyroll.freiberg_flow_stress import FreibergFlowStressCoefficients
from pyroll.report import report


def test_solve_imf_semi_continuous_8_mm_pass_sequence(tmp_path: Path, caplog):
    caplog.set_level(logging.INFO, logger="pyroll")

    in_profile = Profile.round(
        diameter=37e-3,
        temperature=1000 + 273.15,
        strain=0,
        material=["steel", "C20"],
        density=7.5e3,
        specific_heat_capacity=690,
    )

    sequence = PassSequence([
        ThreeRollPass(
            label="13D",
            roll=Roll(
                groove=SwedishOvalGroove(
                    r1=6e-3,
                    r2=26e-3,
                    ground_width=38e-3,
                    usable_width=60e-3,
                    depth=7.25e-3
                ),
                nominal_radius=321e-3 / 2
            ),
            velocity=1,
            gap=13.5e-3,
        ),
        Transport(
            label="13D -> 14D",
            length=1
        ),
    ])

    try:
        sequence.solve(in_profile)
    finally:
        print("\nLog:")
        print(caplog.text)

    report_file = tmp_path / "report.html"

    rendered = report(sequence)
    print()

    report_file.write_text(rendered)

    webbrowser.open(report_file.as_uri())
