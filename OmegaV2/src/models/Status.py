from enum import Enum


class Status(Enum):
    ALL = 'All'
    COMPLETED = 'Completed'
    DROPPED = 'Dropped'
    WATCHING = 'Watching'
    READING = 'Reading'
    PLAN_TO_WATCH = 'Plan to watch'
    PLAN_TO_READ = 'Plan to read'
