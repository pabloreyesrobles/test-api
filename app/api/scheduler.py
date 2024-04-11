from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .utils import *
import subprocess

# Variables globales para rastrear el estado del scheduler y su configuración
scheduler = None
scheduling_enabled = True  # Puede iniciarse en True o False según tus necesidades

current_jobs = {}

# Función para iniciar el scheduler
def start_scheduler():
    global scheduler

    if not scheduler:
        scheduler = BackgroundScheduler()
        scheduler.start()

# Función para detener el scheduler
def stop_scheduler():
    global scheduler
    if scheduler:
        scheduler.shutdown()

def add_task(job_id: str, recurring: bool = False):
    global current_jobs

    # Cron trigger configurado para ejecutar la tarea hora en punto
    cron_trigger = CronTrigger(second=0, minute=0)

    job = scheduler.get_job(job_id)
    if not(job):
        # Ejecutar subproceso
        start_process(job_id)

        # Agregar tarea al scheduler en de que deba revisar el proceso en un intervalo de tiempo
        if recurring:
            scheduler.add_job(recurrent_task, args=(job_id,), trigger=cron_trigger, id=job_id)

def recurrent_task(job_id: str):
    global current_jobs

    return {'message': 'Task executed'}


def start_process(job_id: str):
    global current_jobs
    
    # Comando a ejecutar por terminal
    command = f""

    # Ejecución de proceso simple. Verificar uso de otros argumentos para sofisticar
    current_jobs[job_id]['process'] = subprocess.Popen(command, shell=True, ) 
    current_jobs[job_id]['status'] = 'running'

def stop_process(job_id: str):
    global current_jobs
    if job_id in current_jobs and current_jobs[job_id]['process']:
        current_jobs[job_id]['process'].terminate()
        current_jobs[job_id]['process'].wait()
        current_jobs[job_id]['status'] = 'stopped'

# TODO: Función que se autoejecute si un proceso se detiene

