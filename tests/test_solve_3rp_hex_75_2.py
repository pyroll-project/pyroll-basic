import logging
import webbrowser
from pathlib import Path

from pyroll.basic import Profile, PassSequence, ThreeRollPass, Roll, FlatGroove, Transport
from pyroll.report import report


def test_solve_3rp_hexagon_75_2(tmp_path: Path, caplog):
    caplog.set_level(logging.INFO, logger="pyroll")

    in_profile = Profile.round(
        diameter=96 * 1.0177777e-3,
        temperature=1030 + 273.15,
        strain=0,
        material=["steel", "C20"],
        density=7.5e3,
        specific_heat_capacity=690,
        thermal_conductivity=23
    )

    sequence = PassSequence([
        ThreeRollPass(
            label="Stand - I",
            orientation="Y",
            roll=Roll(
                groove=FlatGroove(
                    r1=5e-3,
                    usable_width=90e-3,
                    pad_angle=30,
                ),
                nominal_radius=293e-3 / 2,
                rotational_frequency=1.73,

            ),
            inscribed_circle_diameter=84.43e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="I->II",
            length=0.72,
        ),
        ThreeRollPass(
            label="Stand - II",
            orientation="AntiY",
            roll=Roll(
                groove=FlatGroove(
                    r1=5e-3,
                    usable_width=90e-3,
                    pad_angle=30,
                ),
                nominal_radius=292.3e-3 / 2,
                rotational_frequency=1.913,

            ),
            inscribed_circle_diameter=80.84e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="II->III",
            length=0.72,
        ),
        ThreeRollPass(
            label="Stand - III",
            orientation="Y",
            roll=Roll(
                groove=FlatGroove(
                    r1=5e-3,
                    usable_width=90e-3,
                    pad_angle=30,
                ),
                nominal_radius=294.5e-3 / 2,
                rotational_frequency=2.09,

            ),
            inscribed_circle_diameter=77.51e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="III->IV",
            length=0.72,
            disk_element_count=10,
        ),
        ThreeRollPass(
            label="Stand - IV",
            orientation="AntiY",
            roll=Roll(
                groove=FlatGroove(
                    r1=5e-3,
                    usable_width=90e-3,
                    pad_angle=30,
                ),
                nominal_radius=296.4e-3 / 2,
                rotational_frequency=2.23,

            ),
            inscribed_circle_diameter=75.8e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="IV->V",
            length=0.72,
        ),
        ThreeRollPass(
            label="Stand - V",
            orientation="Y",
            roll=Roll(
                groove=FlatGroove(
                    r1=5e-3,
                    usable_width=90e-3,
                    pad_angle=30,
                ),
                nominal_radius=301e-3 / 2,
                rotational_frequency=2.27,

            ),
            inscribed_circle_diameter=75.96e-3,
            coulomb_friction_coefficient=0.4,
        )
    ])

    try:
        sequence.solve(in_profile)
    finally:
        print("\nLog:")
        print(caplog.text)

    report_file = tmp_path / "report.html"

    rendered = report(sequence)
    print()

    report_file.write_text(rendered, encoding="utf-8")

    webbrowser.open(report_file.as_uri())
