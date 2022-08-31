from django.contrib import admin
from .models import User
from .models import Condition
from .models import Projects
from .models import Organisation
from .models import Issue
from .models import Agile
from .forms import UserForm
from .forms import ConditionForm
from .forms import ProjectsForm
from .forms import OrganisationForm


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'organisation_names',
                    'project_names', 'role', 'approved', 'organisation_display')
    form = UserForm

    def organisation_display(self, organisation: User.objects):
        organisations = [organisation.organisation_name for organisation in organisation.organisation.all()]
        if len(organisations) > 1:
            return ', '.join(organisations)
        elif len(organisations) == 1:
            return organisations[0]

    organisation_display.short_description = 'Организации'


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('user', 'registration', 'on_validate', 'in_main_menu', 'creating_task', 'creating_comment')
    form = ConditionForm


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'project_name', 'user_names']
    form = ProjectsForm

    def user_names(self, project: Projects.objects):
        users = [user.first_name + ' ' + user.last_name for user in project.users.all()]
        if len(users) > 1:
            return ', '.join(users)
        elif len(users) == 1:
            return users[0]

    user_names.short_description = 'Пользователи'


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['organisation_name', 'user_names']
    form = OrganisationForm

    def user_names(self, organisation: Organisation.objects):
        users = [user.first_name + ' ' + user.last_name for user in organisation.users.all()]
        if len(users) > 1:
            return ', '.join(users)
        elif len(users) == 1:
            return users[0]

    user_names.short_description = 'Пользователи'


@admin.register(Agile)
class AgileAdmin(admin.ModelAdmin):
    list_display = ['agile_name', 'projects', 'user_names']

    def user_names(self, agile: Agile.objects):
        users = [user.first_name + ' ' + user.last_name for user in agile.users.all()]
        if len(users) > 1:
            return ', '.join(users)
        elif len(users) == 1:
            return users[0]

    def projects(self, agile: Agile.objects):
        projects = [project.project_name for project in agile.project_id.all()]
        if len(projects) > 1:
            return ', '.join(projects)
        elif len(projects) == 1:
            return projects[0]


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['user', 'project_id', 'issue_id', 'summary', 'description']
