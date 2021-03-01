from datetime import datetime
from datetime import timedelta


class Hour:

    def __init__(self, d, sunrise, sunset):
        self.sunrise = sunrise
        self.sunset = sunset
        self.temp = 0
        self.humidity = 0
        self.pop = 0
        self.clouds = 0
        self.wind_speed = 0
        self.total_score = 0
        vars(self).update(d)
        self.dt = datetime.fromtimestamp(self.dt)

    def Score(self):
        self.total_score += self.Score_Temperature()
        self.total_score += self.Score_Clouds()
        self.total_score += self.Score_Humidity()
        self.total_score += self.Score_Percipitation()
        self.total_score += self.Score_Wind()
        self.total_score += self.Score_Time()
        self.total_score = int(round(self.total_score))

    def Score_Temperature(self):
        # add .5 point for each degree over or under
        # add 10 points if over 90
        # add 10 points if under 32
        ideal = 72
        score = 0
        score += (abs(ideal - self.temp)*.5)

        if self.temp > 90:
            score + 10

        if self.temp < 32:
            score + 10

        return score

    def Score_Humidity(self):
        # add .5 point for each basis point over or under
        # add 5 points if over or equal to 90 basis points
        ideal = 35
        score = 0

        score += (abs(ideal - self.humidity)*.5)

        if self.humidity >= 90:
            score + 10

        return score

    def Score_Percipitation(self):
        # add 1 point for each basis point over
        ideal = 0
        score = 0
        basis_points = int(round(self.pop * 100))

        for _ in range(ideal, basis_points):
            score += 1

        if basis_points > 80:
            score + 50

        return score

    def Score_Clouds(self):
        # add .25 point for each basis point over or under
        ideal = 25
        score = 0

        score += (abs(ideal - self.clouds)*.25)

        return score

    def Score_Wind(self):
        # add .5 point for each basis point over or under
        # add 10 points if over 15
        ideal = 5
        score = 0

        score += (abs(ideal - self.wind_speed)*.5)

        if self.wind_speed > 15:
            score + 10

        return score

    def Score_Time(self):
        now = datetime.now()
        score = 0

        d = self.dt - now
        d_to_hours = (d.total_seconds()/60)/60

        # is today
        if now.date() == self.dt.date():
            # greater than 8 hours from now; add 5 points
            if d_to_hours > 8:
                score + 5
        # not today
        else:
            # greater than 8 hours from now; add 15 points
            if d_to_hours > 8:
                score + 15

        # is before sunrise; add 3 point
        if now < self.sunrise:
            score + 3
        # is after sunset; add 3 point
        if now > self.sunset:
            score + 3

        return score
