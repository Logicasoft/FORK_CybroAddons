{
    'name': 'Task Statusbar',
    'author': 'Cybrosys Techno Solutions',
    'website': 'www.cybrosys.com',
    'category': 'Project',
    'version': '0.3',
    'summary': 'Calculates the time spend based on assign date and deadline',
    'depends': [
                'base',
                'project',
                ],
    'data': [
            'security/ir.model.access.csv',
            'views/project_statusbar_view.xml',
            ],
    'installable': True,
}
