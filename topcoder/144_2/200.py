class Time:
	def whatTime(self, seconds):
		sec = seconds % 60
		min = int(seconds / 60) % 60
		hour = int(seconds / 3600)
		
		return '{}:{}:{}'.format(hour, min, sec)
