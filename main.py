from functools import partial, update_wrapper
import datetime


class Scheduler:
	def __init__(self):
		self.jobs = []

	def every(self, interval=1):
		job = Job(interval)
		self.jobs.append(job)
		return job

	def run_pending(self):
		all_jobs = (job for job in self.jobs )
		for job in sorted(all_jobs):
			job.run()


class Job:
	def __init__(self, interval):
		self.interval = interval
		self.job_func = None
		self.last_run = None
		self.next_run = None
		self.unit = None
		self.period = None

	def __lt__(self, other):
		return self.next_run < other.next_run

	@property
	def second(self):
		assert self.interval == 1
		return self.seconds

	@property
	def seconds(self):
		self.unit = 'seconds'
		return self
	@property
	def minute(self):
		assert self.interval == 1
		return self.minutes

	@property
	def minutes(self):
		self.unit = 'minutes'
		return self

	@property
	def hour(self):
		assert self.interval == 1
		return self.minutes

	@property
	def hours(self):
		self.unit = 'hours'
		return self

	@property
	def day(self):
		assert self.interval == 1
		return self.day

	@property
	def days(self):
		self.unit = 'days'
		return self

	@property
	def week(self):
		self.unit = 'weeks'
		return self

	@property
	def weeks(self):
		self.unit = 'weeks'
		return self

	@property
	def month(self):
		raise self.interval == 1
		return self.month

	@property
	def months(self):
		self.unit = "months"
		return self   

	def do(self, job_func, *args, **kwargs):
		self.job_func = partial(job_func, *args, **kwargs)
		update_wrapper(self.job_func, job_func)
		self.schedule_next_run()
		return self
    
	def _schedule_next_run (self):
		assert self.unit in ('seconds','minutes','hours','days','weeks','month')
		self.period = datetime.timedelta(**{self.unit:self.interval})
		self.next_run = datetime.datetime.now() + self.period

	def run(self):
		ret = self.job_func()
		self.last_run = datetime.datetime.now()
		self._schedule_next_run()
		return ret


default_scheduler = Scheduler()


def every(interval=1):
	return default_scheduler.every(interval)


def run_pending():
	return default_scheduler.run_pending()
