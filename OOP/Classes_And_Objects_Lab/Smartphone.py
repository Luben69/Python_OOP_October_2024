class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app, app_memory):
        if self.memory >= app_memory and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif self.memory >= app_memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        elif self.memory < app_memory:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"