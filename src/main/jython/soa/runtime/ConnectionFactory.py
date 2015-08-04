class ConnectionFactory(object):

    def __init__(self, deployed):
        self.deployed = deployed

    def get_cf_target(self):
        cf_target = self.deployed.container.name
        if self.deployed.Target:
            cf_target = self.deployed.Target
        return cf_target

    def get_cf_id(self):
        cf_id = self.deployed.name
        if self.deployed.SoaId:
            cf_id = self.deployed.SoaId
        return cf_id
