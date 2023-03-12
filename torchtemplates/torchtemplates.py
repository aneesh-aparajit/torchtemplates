import click
import os
import json
from jinja2 import Environment, PackageLoader
import logging
from rich.logging import RichHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.handlers = [RichHandler(markup=True)]

@click.group()
def torchtemplates():
    pass

@torchtemplates.command()
def init():
    project_name = input('project name: ')
    output_dir   = os.getcwd()
    version      = input('version: ')
    description  = input('description: ')
    git_repo     = input('git repository: ')
    keywords     = input('keywords: ')
    authors      = list(input('authors (enter separated by space if many): ').split(' '))

    print(json.dumps({
        'project_name': project_name, 
        'version': version if not None else '1.0.0',
        'description': description, 
        'git_repo': git_repo, 
        'keywords': keywords, 
        'authors': authors
    }, indent=4))

    ok = input('Is this OK? (yes)')
    if ok is not None and ok.lower() == 'no':
        logger.critical('Aborted.')
        return

    # Create Folder
    if not os.path.exists(os.path.join(output_dir, project_name)):
        os.mkdir(os.path.join(output_dir, project_name))
    else:
        logger.error('Please initialize again with another project name.')
        return
    logger.info('✅ project folder has been created.')
    
    with open(os.path.join('./', project_name, 'metadata.json'), "w") as f:
        json.dump({
            'project_name': project_name, 
            'version': version if not None else '1.0.0',
            'description': description, 
            'git_repo': git_repo, 
            'keywords': keywords, 
            'authors': authors
        }, f)
    
    # Requirements.txt
    try:
        with open(os.path.join(output_dir, project_name, 'requirements.txt'), 'w') as f:
            f.write('# Add the dependencies here...')
        logger.info('✅ requirements.txt has been created.')
    except Exception as e:
        logger.error(f'Something unexpected occured...')
        logger.error(e.__str__)
        return
    
    # Setup.py
    try:
        env = Environment(loader=PackageLoader('torchtemplates', 'templates'))
        template = env.get_template('setup.py.j2')
        rendered_template = template.render(
            project_name=project_name, 
            version=version, 
            authors=authors, 
            description=description, 
            keywords=keywords, 
            git_url="" if git_repo is None else git_repo
        )

        with open(os.path.join(output_dir, project_name, 'setup.py'), 'w') as f:
            f.write(rendered_template)
        
        logger.info('✅ setup.py has been created.')
    except Exception as e:
        logger.error(f'Something unexpected occured...')
        logger.error(e.__str__)
        return
    

@torchtemplates.command()
@click.argument('datatype')
@click.argument('projectname')
def new_pipeline(datatype: str, projectname: str):
    PROJECT_FOLDER = projectname
    if datatype not in ['text', 'tabular', 'image']:
        raise NotImplementedError(f"Datasets for {datatype} has not been implemented... Try implementing from ['text', 'tabular', 'image']")

    output_dir = os.getcwd()
    # Create outputdir/PROJECT_FOLDER/config/
    if os.path.exists(os.path.join(output_dir, PROJECT_FOLDER, 'config/')):
        logger.error(f'Config folder at {os.path.join(output_dir, PROJECT_FOLDER, "config/")} already exists...')
        return
    else:
        os.mkdir(os.path.join(output_dir, PROJECT_FOLDER, 'config/'))

    # Create outputdir/PROJECT_FOLDER/PROJECT_FOLDER
    if os.path.exists(os.path.join(output_dir, PROJECT_FOLDER, PROJECT_FOLDER)):
        logger.error(f'Config folder at {os.path.join(output_dir, PROJECT_FOLDER, PROJECT_FOLDER)} already exists...')
        return
    else:
        os.mkdir(os.path.join(output_dir, PROJECT_FOLDER, PROJECT_FOLDER))
    
    # create config.py
    try: 
        env = Environment(loader=PackageLoader('torchtemplates', 'templates'))
        template = env.get_template('config.py.j2')
        rendered_template = template.render()

        with open(os.path.join(output_dir, PROJECT_FOLDER, 'config', 'config.py'), 'w') as f:
            f.write(rendered_template)
        
        logger.info('✅ config/config.py has been created.')

    except Exception as e:
        logger.error(f'Something unexpected occured...')
        logger.error(e.__str__)
        return
    
    # model.py
    try: 
        env = Environment(loader=PackageLoader('torchtemplates', 'templates'))
        template = env.get_template('model.py.j2')
        rendered_template = template.render()

        with open(os.path.join(output_dir, PROJECT_FOLDER, PROJECT_FOLDER, 'model.py'), 'w') as f:
            f.write(rendered_template)
        
        logger.info(f'✅ {PROJECT_FOLDER}/model.py has been created.')

    except Exception as e:
        logger.error(f'Something unexpected occured...')
        logger.error(e.__str__)
        return

    # training.py
    try: 
        env = Environment(loader=PackageLoader('torchtemplates', 'templates'))
        template = env.get_template('training.py.j2')
        rendered_template = template.render()

        with open(os.path.join(output_dir, PROJECT_FOLDER, PROJECT_FOLDER, 'training.py'), 'w') as f:
            f.write(rendered_template)
        
        logger.info(f'✅ {PROJECT_FOLDER}/training.py has been created.')

    except Exception as e:
        logger.error(f'Something unexpected occured...')
        logger.error(e.__str__)
        return

    # dataset.py
    try: 
        env = Environment(loader=PackageLoader('torchtemplates', 'templates'))
        template = env.get_template(f'{datatype}_data.py.j2')
        rendered_template = template.render()

        with open(os.path.join(output_dir, PROJECT_FOLDER, PROJECT_FOLDER, 'dataset.py'), 'w') as f:
            f.write(rendered_template)
        
        logger.info(f'✅ {PROJECT_FOLDER}/dataset.py has been created.')

    except Exception as e:
        logger.error(f'Something unexpected occured...')
        logger.error(e.__str__)
        return
    
    # create_folds.py
    try: 
        env = Environment(loader=PackageLoader('torchtemplates', 'templates'))
        template = env.get_template('create_folds.py.j2')
        rendered_template = template.render()

        with open(os.path.join(output_dir, PROJECT_FOLDER, PROJECT_FOLDER, 'create_folds.py'), 'w') as f:
            f.write(rendered_template)
        
        logger.info(f'✅ {PROJECT_FOLDER}/create_folds.py has been created.')

    except Exception as e:
        logger.error(f'Something unexpected occured...')
        logger.error(e.__str__)
        return
    
    # utils.py
    try: 
        env = Environment(loader=PackageLoader('torchtemplates', 'templates'))
        template = env.get_template('utils.py.j2')
        rendered_template = template.render()

        with open(os.path.join(output_dir, PROJECT_FOLDER, PROJECT_FOLDER, 'utils.py'), 'w') as f:
            f.write(rendered_template)
        
        logger.info(f'✅ {PROJECT_FOLDER}/utils.py has been created.')

    except Exception as e:
        logger.error(f'Something unexpected occured...')
        logger.error(e.__str__)
        return
    
    logger.info(f'✅ {PROJECT_FOLDER} repo has been created.')


if __name__ == "__main__":
    torchtemplates()
