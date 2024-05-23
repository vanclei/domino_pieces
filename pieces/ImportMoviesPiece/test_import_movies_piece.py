from domino.testing import piece_dry_run

def test_import_movies_get():
    input_data = {
        'movies_data_path': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        'gain_reference_path': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        'defect_file_path': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    }
    piece_output = piece_dry_run(
        piece_name="ImportMoviesPiece",
        input_data=input_data
    )
    assert piece_output['image_file_path'] == 'dry_run_results/modified_image.png'
