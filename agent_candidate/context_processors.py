from agent_candidate import models
from job_advertisement.models import MyTodoModel
from datetime import datetime, timedelta

def folderslists(request):
    t = datetime.today() + timedelta(hours=5, minutes=30)
    t = datetime.strptime(t.strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M')
    folders = models.FoldersModel.objects.all()
    title_folders = models.CreateTitleFolderModel.objects.all()
    try:
        todo_cnt = MyTodoModel.objects.filter(user=request.user, deadline__lte=t, is_completed=False).count()
    except:
        todo_cnt = 0
    datas = {'folders': folders, 'title_folders': title_folders, 'todo_cnt': todo_cnt}
    return datas