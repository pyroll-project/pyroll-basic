import logging
import webbrowser
from pathlib import Path

from pyroll.basic import Profile, PassSequence, RollPass, Roll, DiamondGroove, Transport, SquareGroove, RoundGroove, \
    CircularOvalGroove
from pyroll.freiberg_flow_stress import FreibergFlowStressCoefficients
from pyroll.report import report


def test_solve_imf_semi_continuous_8_mm_pass_sequence(tmp_path: Path, caplog):
    caplog.set_level(logging.INFO, logger="pyroll")

    in_profile = Profile.square(
        side=45e-3,
        corner_radius=3e-3,
        temperature=1100 + 273.15,
        strain=0,
        material=["C45", "steel"],
        freiberg_flow_stress_coefficients=FreibergFlowStressCoefficients(
            a=2731.39 * 1e6,
            m1=-0.00268,
            m2=0.31076,
            m3=0,
            m4=-0.00056,
            m5=0.00046,
            m6=0,
            m7=-0.98375,
            m8=0.000139,
            m9=0,
            baseStrain=0.1,
            baseStrainRate=0.1
        ),
        density=7.5e3,
        specific_heat_capacity=690,
        thermal_conductivity=23
    )

    mean_roll_radius_1_upper = (328e-3 + 324e-3) / 2 / 2
    mean_roll_radius_1_lower = (324e-3 + 320e-3) / 2 / 2
    mean_roll_radius_2_upper = (299e-3 + 297e-3) / 2 / 2
    mean_roll_radius_2_lower = (297e-3 + 295e-3) / 2 / 2
    
    transport_duration = 2

    sequence = PassSequence([
    RollPass(
        label="Diamond I",
        roll=Roll(
            groove=DiamondGroove(
                usable_width=76.55e-3,
                tip_depth=22.1e-3,
                r1=12e-3,
                r2=8e-3
            ),
            nominal_radius=mean_roll_radius_1_lower,
            
        ),
        velocity=1,
        gap=3e-3,
    ),
    Transport(
        duration=transport_duration
    ),
    RollPass(
        label="Square II",
        roll=Roll(
            groove=SquareGroove(
                usable_width=52.7e-3,
                tip_depth=25.95e-3,
                r1=8e-3,
                r2=6e-3
            ),
            nominal_radius=mean_roll_radius_1_upper,
            
        ),
        velocity=1,
        gap=3e-3,
    ),
    Transport(
        duration=transport_duration
    ),
    RollPass(
        label="Diamond III",
        roll=Roll(
            groove=DiamondGroove(
                usable_width=58.3e-3,
                tip_depth=16.85e-3,
                r1=7e-3,
                r2=8e-3
            ),
            nominal_radius=mean_roll_radius_1_lower,
            
        ),
        velocity=1,
        gap=3e-3,
    ),
    Transport(
        duration=transport_duration
    ),
    RollPass(
        label="Square IV",
        roll=Roll(
            groove=SquareGroove(
                usable_width=40.74e-3,
                tip_depth=20.05e-3,
                r1=7e-3,
                r2=5e-3
            ),
            nominal_radius=mean_roll_radius_1_upper,
            
        ),
        velocity=1,
        gap=3e-3,
    ),
    Transport(
        duration=transport_duration
    ),
    RollPass(
        label="Oval V",
        roll=Roll(
            groove=CircularOvalGroove(
                depth=7.25e-3,
                r1=6e-3,
                r2=44.5e-3
            ),
            nominal_radius=mean_roll_radius_1_lower,
            
        ),
        velocity=1,
        gap=3e-3,
    ),
    Transport(
        duration=transport_duration
    ),
    RollPass(
        label="Square VI",
        roll=Roll(
            groove=SquareGroove(
                usable_width=29.64e-3,
                tip_depth=14.625e-3,
                r1=6e-3,
                r2=4e-3
            ),
            nominal_radius=mean_roll_radius_1_upper,
        ),
        velocity=1,
        gap=3e-3,
    ),
    Transport(
        duration=transport_duration
    ),
    RollPass(
        label="Oval VII",
        roll=Roll(
            groove=CircularOvalGroove(
                depth=5.05e-3,
                r1=7e-3,
                r2=33e-3
            ),
            nominal_radius=mean_roll_radius_1_lower,
            
        ),
        velocity=1,
        gap=3e-3,
    ),
    Transport(
        duration=transport_duration
    ),
    RollPass(
        label="Square VIII",
        roll=Roll(
            groove=SquareGroove(
                usable_width=21.54e-3,
                tip_depth=10.6e-3,
                r1=5e-3,
                r2=3e-3
            ),
            nominal_radius=mean_roll_radius_1_upper,
            
        ),
        velocity=1,
        gap=3e-3,
    ),
    Transport(
        duration=transport_duration
    ),
    RollPass(
        label="Oval IX",
        roll=Roll(
            groove=CircularOvalGroove(
                depth=4.43e-3,
                r1=6e-3,
                r2=25.5e-3
            ),
            nominal_radius=mean_roll_radius_2_lower,
            
        ),
        velocity=1,
        gap=1e-3,
    ),
    Transport(
        duration=transport_duration
    ),
    RollPass(
        label="Round Xa",
        roll=Roll(
            groove=RoundGroove(
                r1=2e-3,
                r2=15.8e-3 / 2,
                depth=7.65e-3
            ),
            nominal_radius=mean_roll_radius_2_upper,
            
        ),
        velocity=1,
        gap=0.5e-3,
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
