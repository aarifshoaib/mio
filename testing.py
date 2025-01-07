import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mio.settings')
django.setup()

from django.db.models import Q, Count
from client_management import models
# from agent_candidate import models

# orders = models.CreateOrderModel.objects.filter(
#                                     Q(pass_type__istartswith='DP')).filter(application_id__isnull=True)
# print(orders)

# x = models.CreateUserModel.objects.all()
# for i in x:
#     print(i.user.username, i.view_password, i.user.is_active, i.user.last_login)
# print(dir(x.first().user))

# orders = models.CreateOrderModel.objects.all()
# for ord in orders:
#     if ord.voice_record:
#         print(ord.id, ord.voice_record, ord.dropbox_url, ord.tiny_url)

# from pydub import AudioSegment
# from pydub.playback import play

# def with_file():
#     # Load your audio file
#     audio = AudioSegment.from_file("audio_gTTJRcK.mp3")

#     # Change the pitch (octaves, can be negative or positive)
#     def change_pitch(sound, octaves):
#         new_sample_rate = int(sound.frame_rate * (0.8 ** octaves))
#         return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate}).set_frame_rate(sound.frame_rate)

#     # Change the speed (factor can be > 1 for speed up, < 1 for slow down)
#     def change_speed(sound, factor):
#         return sound._spawn(sound.raw_data, overrides={
#             "frame_rate": int(sound.frame_rate * factor)
#         }).set_frame_rate(sound.frame_rate)

#     # Example: increase pitch by 1 octave and speed by 1.5 times
#     modified_audio = change_pitch(audio, 1)
#     modified_audio = change_speed(modified_audio, 1.6)

#     # Save the modified audio
#     modified_audio.export("modified_audio.mp3", format="mp3")



# from pydub import AudioSegment
# from io import BytesIO
# from pydub.utils import which

# AudioSegment.converter = which("ffmpeg")

# def change_pitch(sound, octaves):
#     new_sample_rate = int(sound.frame_rate * (0.8 ** octaves))
#     return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate}).set_frame_rate(sound.frame_rate)

# def change_speed(sound, factor):
#     return sound._spawn(sound.raw_data, overrides={
#         "frame_rate": int(sound.frame_rate * factor)
#     }).set_frame_rate(sound.frame_rate)

# def process_audio(audio_bytes, pitch_change, speed_change):
#     audio = AudioSegment.from_file(audio_bytes)
#     modified_audio = change_pitch(audio, pitch_change)
#     modified_audio = change_speed(modified_audio, speed_change)

#     out_bytes = BytesIO()
#     modified_audio.export(out_bytes, format="mp3")
#     out_bytes.seek(0)

#     return out_bytes

# with open('audio_gTTJRcK.mp3', 'rb') as audio:
#     audio_bytes = audio.read()

# modified_audio_bytes = process_audio('audio_gTTJRcK.mp3', 1, 1.6)
# print(modified_audio_bytes)

import os

folders = '''
		AMC_upload_cert
		AMC_upload_passport
		AMC_upload_resume
		AMC_upload_video
		AMC_upload_work_video
		AgentManagementCandidateFiles
		AppQueueVoiceRecord
		ApplicationQueue
		ApplicationQueueFiles
		BuyingSelling
		CPF_CSV_Invoice
		CPF_Entry_Form1_IC_Copy
		CPF_Entry_Form2_DraftUpload
		CPF_PDF_Invoice
		CardStatus
		CreateOrder
		CreateTask
		EPOL_ApplyCopy
		EPOL_Reject_Reason
		EmailAttachments
		ICA_File
		IssueDocs
		Pending_Doc
		Sample Files
		UploadIPA
		VoiceRecord
		notify_acknowledgement
		'''
folders = [f.strip() for f in folders.splitlines() if f ]

for folder in folders:
    fpath = f'/home/myindiaoverseas/mio/media/{folder}'
    fobj = open(f'files_fold/{folder}.txt', 'w')

    for root, folders, files in os.walk(fpath):
        for file in files:
            ffile = os.path.join(root, file)
            fobj.write(f'{ffile}\n')
            # print(ffile)