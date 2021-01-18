from modules.jobs import pre_proc

from modules.utils.logger_utils import get_logger

jobs = {
    'pre_proc': pre_proc.process
}


def run(parameters):
    logger = get_logger()

    for parameter, value in parameters.items():
        logger.info('Param {param}: {value}'.format(
            param=parameter, value=value))

    job_name = parameters['job_name']

    process_function = jobs[job_name]
    process_function(
        input_path=parameters['input_path'],
        output_path=parameters['output_path']
    )
