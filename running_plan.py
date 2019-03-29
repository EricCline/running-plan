class Week(object):

    def __init__(self, total):
        self.total = round(total, 2)
        self.days = self.calculate()

    def calculate(self):
        pass

    def __repr__(self):
        return "total: {} - {}".format(self.total, self.days)


class EarlyWeek(Week):

    def calculate(self):
        return (
            round(self.total * .3, 2),
            round(self.total * .3, 2),
            round(self.total * .4, 2)
        )


class LateWeek(Week):

    def calculate(self):
        return (
            round(self.total * .2, 2),
            round(self.total * .3, 2),
            round(self.total * .5, 2)
        )

class Plan(object):

    def __init__(self, num_weeks, percent_increase, starting_mileage):
        self.num_weeks = num_weeks
        self.percent_increase = percent_increase
        self.starting_mileage = starting_mileage
        self.weeks = self.calculate()

    def calculate(self):
        weeks = [self.WEEK_TYPE(self.starting_mileage)]
        for _ in range(self.num_weeks -1):
            weeks.append(self.WEEK_TYPE(weeks[-1].total * self.percent_increase))
        return weeks

    def __repr__(self):
        return "\n".join(
            "week {}: {}".format(
                i+1,
                repr(w)
            ) for i, w in enumerate(self.weeks)
        )


class FoundationPlan(Plan):

    WEEK_TYPE = EarlyWeek


class DistancePlan(Plan):

    WEEK_TYPE = LateWeek




print(FoundationPlan(8, 1.1, 5))
print(DistancePlan(12, 1.07, 9.75))
