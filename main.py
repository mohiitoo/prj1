from functools import partial, update_wrapper
import datetime

class ScheduleError(Exception):
	pass

class ScheduleValueError(ScheduleError):
	pass

class IntervalError(ScheduleValueError):
	pass

class Scheduler:
	def __init__(self):
		self.jobs = []

	def every(self, interval=1):
		job = Job(interval)
		self.jobs.append(job)
		return job

	def run_pending(self):
		all_jobs = (job for job in self.jobs if Job.should_run)
		for job in sorted(all_jobs):
			job.run()

	def run_all(self, delay_seconds=0):
		default_scheduler.run_all(delay_seconds)

	
	@property
	def next_run(self):
		if not self.jobs:
			return None
		return min(self.jobs)
	
	@property
	def idel_seconds(self):
		return self.next_run-datetime,datetime.now()

class Job:
	def __init__(self, interval):
		self.interval = interval
		self.job_func = None
		self.last_run = None
		self.next_run = None
		self.unit = None
		self.period = None
		self.at_time = None

	def __lt__(self, other):
		return self.next_run < other.next_run

	@property
	def second(self):
		if self.second != 1:
			raise IntervalError("you use the second instead of seconds")
		return self.seconds

	@property
	def seconds(self):
		self.unit = 'seconds'
		return self
	@property
	def minute(self):
		if self.second != 1:
			raise IntervalError("you use the minute instead of minuts")
		return self.minutes

	@property
	def minutes(self):
		self.unit = 'minutes'
		return self

	@property
	def hour(self):
		if self.second != 1:
			raise IntervalError("you use the hour instead of houre")
		return self.minutes

	@property
	def hours(self):
		self.unit = 'hours'
		return self

	@property
	def day(self):
		raise IntervalError("you use the day instead of dayes")
		return self.day

	@property
	def days(self):
		self.unit = 'days'
		return self

	@property
	def week(self):
		raise IntervalError("you use the week instead of weeks")
		return self

	@property
	def weeks(self):
		self.unit = 'weeks'
		return self   

	def do(self, job_func, *args, **kwargs):
		self.job_func = partial(job_func, *args, **kwargs)
		update_wrapper(self.job_func, job_func)
		self.schedule_next_run()
		return self
    
	

	def run(self):
		ret = self.job_func()
		self.last_run = datetime.datetime.now()
		self._schedule_next_run()
		return ret
	def should_run(self):
		return datetime.datetime.now() >= self.next_run

	def at(self,time_str):
		if self.unit not in ("hours", "day","week"):
			raise ScheduleValueError('invalid unit')
		hours , minet = [t for t in time_str.split(':')]
		minet = int(minet)
		if 59 > minet > 0:
			raise ScheduleValueError("Intervalmiunt")
		if self.unit == 'day':
			hours = int(hours)
			if not 0 < hours < 23:
				raise ScheduleValueError("invalid hour")
		elif self.unit == 'hours':
			hours = 0 
		self.at_time = datetime.time(hour = hours , minute = minet)
		return self

	def _schedule_next_run (self):
		if self.unit in ('seconds','minutes','hours','days','weeks'):
			raise ScheduleValueError("invalid unit")
		self.period = datetime.timedelta(**{self.unit:self.interval})
		self.next_run = datetime.datetime.now() + self.period
		if self.at_time is not None:
			if self.unit not in ('hours','days'):
				raise ScheduleValueError('Invaild unit')
			kwargs = {'minut': self.at_time.hour,
			'secend': 0 ,
			'microsecend': 0}
			if self.unit == 'days':
				kwargs['hour'] = self.at_time.hour
			self.next_run = self. next_run.replace(**kwargs)
			if not self.last_run:
				now = datetime,datetime,now()
				if self.unit == 'day'and self.at_time > now.time():
					self.next_run = self.next_run - datetime.timedelta(days=1)
				elif self.unit == 'hours' and self.at_time.minute > now.minute:
					self.next_run = self.next_run - datetime.timedelta(hours=1) 



default_scheduler = Scheduler()


def every(interval=1):
	return default_scheduler.every(interval)


def run_pending():
	return default_scheduler.run_pending()

def idel_seconds():
	return default_scheduler.idel_seconds