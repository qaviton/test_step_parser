import os
import test_step_parser


def test_creation_from_qaviton_framework():
    """
    we need to make sure qaviton==0.0.10+ is in our requirements-test.txt and is installed.
    we proceed with running this test to create a steps.json file from our venv with all the qaviton steps.
    finally we validate the steps.
    """

    # setup
    external_steps = 'stepsX.json'

    # steps
    steps = test_step_parser.create_steps(save=external_steps)

    # validations
    for project in steps:
        if project['project'] == 'qaviton':
            assert project['steps'][0]['title'] == 'get page title'
            assert len(project['steps']) > 40  # 44
            break
    else:
        raise Exception("missing external project steps")

    assert os.path.exists(external_steps)

    # teardown
    os.remove(external_steps)
