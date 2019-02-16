import test_step_parser


def test_creation_from_qaviton_framework():
    """
    we need to make sure qaviton==0.0.8+ is in our requirements-test.txt and is installed.
    we proceed with running this test to create a steps.json file from our venv with all the qaviton steps.
    finally we validate the steps.
    """
    # TODO: need to add logic
    test_step_parser.create()
    # validate steps.json file


