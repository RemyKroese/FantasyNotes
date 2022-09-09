import backend.models as m


class Notebook:
    def __init__(self):
        self.campaigns = []
        self.current_campaign = None

    def add_campaign(self, name):
        self.campaigns.append(m.Campaign(name))

    def open_campaign(self, campaign):
        self.current_campaign = campaign


def load_data():
    return True


if __name__ == "__main__":
    print('Hello World')
