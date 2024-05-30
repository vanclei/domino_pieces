from domino.testing import piece_dry_run

def test_AdditionalRefinementPiece_piece():
    input_data = dict(
        input_image='test.png'
    )
    output_data = piece_dry_run(
        "AdditionalRefinementPiece",
        input_data,
    )
    assert output_data["image_base64_string"] is not None