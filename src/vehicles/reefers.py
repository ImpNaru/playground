from ship import Reefer


def main():
    ship = Reefer(
        numeric_id=61,
        name="Langara",
        gen=3,
        subtype="B",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = Reefer(
        numeric_id=60,
        name="Samphire",
        gen=3,
        subtype="C",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=6,
    )

    ship = Reefer(
        numeric_id=14,
        name="Kodiak",
        gen=3,
        subtype="D",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = Reefer(
        numeric_id=59,
        name="Caribou",
        gen=3,
        subtype="E",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
    )

    ship = Reefer(
        numeric_id=15,
        name="Helsinki",
        gen=3,
        subtype="F",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
