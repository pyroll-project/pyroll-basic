import logging
import webbrowser
from pathlib import Path

from pyroll.basic import Profile, PassSequence, RollPass, Roll, Transport, Oval3RadiiGroove, FalseRoundGroove, Oval3RadiiFlankedGroove, BoxGroove

from pyroll.freiberg_flow_stress import FreibergFlowStressCoefficients
from pyroll.report import report


def test_solve_sag_kalibreur_pass_sequence(tmp_path: Path, caplog):
    caplog.set_level(logging.INFO, logger="pyroll")

    in_profile = Profile.box(
        label='Box 180²',
        height=(180 * 1.0177777) * 1e-3,
        width=(180 * 1.0177777) * 1e-3,
        temperature=1180 + 273.15,
        corner_radius=5e-3,
        material=["11SMn30/1.0715", "free-cutting steel"],
        freiberg_flow_stress_coefficients=FreibergFlowStressCoefficients(
            a=1473.43 * 1e6,
            m1=-0.00239,
            m2=0.22924,
            m3=0,
            m4=-0.00870,
            m5=0.00010,
            m6=0,
            m7=-0.44065,
            m8=0.000161,
            m9=0,
            baseStrain=0.1,
            baseStrainRate=0.1,
        ),
        density=7.5e3,
        specific_heat_capacity=690,
        thermal_conductivity=23,
    )

    sequence = PassSequence([
        RollPass(
            label="Pass 1 | Stand 1 | BX1",
            roll=Roll(
                groove=BoxGroove(
                    r1=12e-3,
                    r2=18e-3,
                    depth=43.5e-3,
                    usable_width=215e-3,
                    flank_angle=82,
                ),
                nominal_radius=655e-3 / 2,
            ),
            velocity=0.798,
            gap=53e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="I -> II",
            length=3.8,
        ),
        RollPass(
            label="Pass 2 | Stand 2 | RD17.6",
            roll=Roll(
                groove=BoxGroove(
                    r1=10e-3,
                    r2=18e-3,
                    depth=44.5e-3,
                    ground_width=146.5e-3,
                    usable_width=168e-3,
                ),
                nominal_radius=655e-3 / 2,
            ),
            velocity=9.993,
            gap=53e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="II -> III",
            length=3.8,
        ),
        RollPass(
            label="K 02/001 - 3",
            roll=Roll(
                label="Pass 3 | Stand 3 | BX150y",
                groove=BoxGroove(
                    r1=10e-3,
                    r2=18e-3,
                    depth=35e-3,
                    ground_width=146e-3,
                    usable_width=169e-3,
                ),
                nominal_radius=655e-3 / 2,
            ),
            velocity=1.246,
            gap=43e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="III -> IV",
            length=3.8,
        ),
        RollPass(
            label="Pass 4 | Stand 4 | BO119a",
            roll=Roll(
                groove=Oval3RadiiFlankedGroove(
                    usable_width=134e-3,
                    flank_angle=90 - 13.4,
                    depth=41.5e-3,
                    r1=10e-3,
                    r2=18e-3,
                    r3=200e-3,
                ),
                nominal_radius=655e-3 / 2,
            ),
            velocity=1.453,
            gap=44e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="IV -> V",
            length=58.1
        ),
        RollPass(
            label="Pass 5 | Stand 5 | BOg3z",
            roll=Roll(
                groove=Oval3RadiiGroove(
                    r1=15e-3,
                    r2=70e-3,
                    r3=150e-3,
                    depth=33e-3,
                    usable_width=160e-3,
                ),
                nominal_radius=567e-3 / 2,
            ),
            velocity=0.864,
            gap=39e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="V -> VI",
            length=3.5
        ),
        RollPass(
            label="Pass 6 | Stand 6 | RD111",
            roll=Roll(
                groove=FalseRoundGroove(
                    r1=10e-3,
                    r2=55.5e-3,
                    depth=48e-3,
                    flank_angle=60,
                ),
                nominal_radius=530e-3 / 2,
            ),
            velocity=1.057,
            gap=19e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="VI -> VII",
            length=3.5
        ),
        RollPass(
            label="Pass 7 | Stand 7 | BO69.6e",
            roll=Roll(
                groove=Oval3RadiiGroove(
                    r1=15e-3,
                    r2=50e-3,
                    r3=115e-3,
                    depth=28.3e-3,
                    usable_width=125e-3,
                ),
                nominal_radius=490e-3 / 2,
            ),
            velocity=1.186,
            gap=33.5e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="VII -> IIX",
            length=3.5
        ),
        RollPass(
            label="Pass 8 | Stand 8 | S96",
            roll=Roll(
                groove=Oval3RadiiGroove(
                    r1=6e-3,
                    r2=150e-3,
                    r3=48e-3,
                    depth=42.5e-3,
                    usable_width=110e-3,
                ),
                nominal_radius=530e-3 / 2,
            ),
            velocity=1.437,
            gap=10e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="IIX -> IX",
            length=9.3
        ),
        RollPass(
            label="Pass 9 | Stand 9 | P96",
            roll=Roll(
                groove=Oval3RadiiGroove(
                    r1=6e-3,
                    r2=87.01e-3,
                    r3=48e-3,
                    depth=43e-3,
                    usable_width=97.92e-3,
                ),
                nominal_radius=382.5e-3 / 2,
            ),
            velocity=1.5,
            gap=10e-3,
            coulomb_friction_coefficient=0.4,
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

    report_file.write_text(rendered, encoding="utf-8")

    webbrowser.open(report_file.as_uri())
