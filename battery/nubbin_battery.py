
from dateutil.relativedelta import relativedelta
from battery import Battery


class NubbinBattery(Battery):
    def _init_(self, last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        should_be_service_date = self.last_service_date + relativedelta(years=2)
        return self.current_date > should_be_service_date
   
