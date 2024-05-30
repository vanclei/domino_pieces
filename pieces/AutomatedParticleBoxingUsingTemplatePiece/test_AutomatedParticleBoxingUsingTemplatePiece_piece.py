from domino.testing import piece_dry_run
    
def test_AutomatedParticleBoxingUsingTemplatePiece_piece():
    input_data = dict(
        input_image='test.png'
    )
    output_data = piece_dry_run(
        "AutomatedParticleBoxingUsingTemplatePiece",
        input_data,
    )
    assert output_data["image_base64_string"] is not None        