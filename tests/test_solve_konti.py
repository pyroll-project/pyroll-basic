import logging
import webbrowser
from pathlib import Path

from pyroll.basic import Profile, PassSequence, RollPass, Roll, CircularOvalGroove, Transport, RoundGroove, \
    SwedishOvalGroove
from pyroll.freiberg_flow_stress import FreibergFlowStressCoefficients
from pyroll.report import report


def test_solve(tmp_path: Path, caplog):
    caplog.set_level(logging.INFO, logger="pyroll")

    in_profile = Profile.round(
        radius=24e-3,
        temperature=1200 + 273.15,
        strain=0,
        material="BST 500",
        freiberg_flow_stress_coefficients=FreibergFlowStressCoefficients(
            a=4877.12 * 1e6,
            m1=-0.00273339,
            m2=0.302309,
            m3=-0.0407581,
            m4=0.000222222,
            m5=-0.000383134,
            m6=0,
            m7=-0.492672,
            m8=0.0000175044,
            m9=-0.0611783,
            baseStrain=0.1,
            baseStrainRate=0.1
        ),
        density=7.5e3,
        thermal_capacity=690,
    )

    sequence = PassSequence([
        RollPass(
            label="K 02/001 - 1",
            roll=Roll(
                groove=SwedishOvalGroove(
                    r1=6e-3,
                    r2=26e-3,
                    ground_width=38e-3,
                    usable_width=60e-3,
                    depth=7.25e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=1,
            gap=13.5e-3,
        ),
        Transport(
            label="I -> II",
            duration=6.4
        ),
        RollPass(
            label="K 05/001 - 2",
            roll=Roll(
                groove=RoundGroove(
                    r1=4e-3,
                    r2=18e-3,
                    depth=17.5e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=1,
            gap=1.5e-3,
        ),
        Transport(
            label="II -> III",
            duration=3.6
        ),
        RollPass(
            label="K 02/001 - 3",
            roll=Roll(
                groove=SwedishOvalGroove(
                    r1=6e-3,
                    r2=26e-3,
                    ground_width=38e-3,
                    usable_width=60e-3,
                    depth=7.25e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=2,
            gap=1.5e-3,
        ),
        Transport(
            label="III -> IV",
            duration=3.4
        ),
        RollPass(
            label="K 05/002 - 4",
            roll=Roll(
                groove=RoundGroove(
                    r1=4e-3,
                    r2=13.5e-3,
                    depth=12.5e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=2,
            gap=1e-3,
        ),
        Transport(
            label="IV -> V",
            duration=5.2
        ),
        RollPass(
            label="K 03/001 - 5",
            roll=Roll(
                groove=CircularOvalGroove(
                    r1=6e-3,
                    r2=38e-3,
                    depth=4e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=2,
            gap=5.4e-3,
        ),
        Transport(
            label="V -> VI",
            duration=4.4
        ),
        RollPass(
            label="K 05/003 - 6",
            roll=Roll(
                groove=RoundGroove(
                    r1=3e-3,
                    r2=10e-3,
                    depth=9e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=2,
            gap=1.8e-3,
        ),
        Transport(
            label="VI -> VII",
            duration=3.8
        ),
        RollPass(
            label="K 03/001 - 7",
            roll=Roll(
                groove=CircularOvalGroove(
                    r1=6e-3,
                    r2=38e-3,
                    depth=4e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=2,
            gap=0.8e-3,
        ),
        Transport(
            label="VII -> IIX",
            duration=7.2
        ),
        RollPass(
            label="K 05/004 - 8",
            roll=Roll(
                groove=RoundGroove(
                    r1=2e-3,
                    r2=7.5e-3,
                    depth=5.5e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=2,
            gap=3.8e-3,
        ),
        Transport(
            label="IIX -> IX",
            duration=6.2
        ),
        RollPass(
            label="K 03/002 - 9",
            roll=Roll(
                groove=CircularOvalGroove(
                    r1=6e-3,
                    r2=21.2e-3,
                    depth=2.5e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=2,
            gap=3.5e-3,
        ),
        Transport(
            label="IX -> X",
            duration=4.5
        ), RollPass(
            label="K 05/005 - 10",
            roll=Roll(
                groove=RoundGroove(
                    r1=0.5e-3,
                    r2=6e-3,
                    depth=4e-3
                ),
                nominal_radius=321e-3 / 2,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=2,
            gap=4e-3,
        ),
        Transport(
            label="X -> XI",
            duration=9
        ),
        RollPass(
            label="F1 - K 3/50",
            roll=Roll(
                groove=CircularOvalGroove(
                    r1=2.5e-3,
                    r2=12.5e-3,
                    depth=2.9e-3
                ),
                nominal_radius=107.5e-3,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=4.89,
            gap=1.2e-3,
        ),
        Transport(
            label="XI -> XII",
            duration=1.5 / 4.89
        ),
        RollPass(
            label="F2 - K 9/24",
            roll=Roll(
                groove=RoundGroove(
                    r1=0.5e-3,
                    r2=5.1e-3,
                    depth=4.25e-3
                ),
                nominal_radius=107.5e-3,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=6.1,
            gap=0.9e-3,
        ),
        Transport(
            label="XII -> XIII",
            duration=1.5 / 6.1
        ),
        RollPass(
            label="F3 - K3/51",
            roll=Roll(
                groove=CircularOvalGroove(
                    r1=2.5e-3,
                    r2=11e-3,
                    depth=2.12e-3
                ),
                nominal_radius=107.5e-3,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=7.91,
            gap=1.75e-3,
        ),
        Transport(
            label="I -> II",
            duration=1.5 / 7.91
        ),
        RollPass(
            label="F4 - K 9/23",
            roll=Roll(
                groove=RoundGroove(
                    r1=0.5e-3,
                    r2=3.5e-3,
                    depth=3.5e-3
                ),
                nominal_radius=85e-3,
                elastic_modulus=210e9,
                poissons_ratio=0.3
            ),
            velocity=10,
            gap=1.5e-3,
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
