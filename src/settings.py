import os
import pandas as pd

class CONFIG:
    
    attr1 = 1
    attr2 = "helloworld"
    attr3 = {"k": "v"}

    scenario = "base_scenario"
    fp_data = os.path.join("data", scenario, "data.csv")

    @classmethod
    def update(cls, scenario: str, verbose: bool = False):
        """Update configuration based on scenario.

        Args:
            scenario (str): scenario to use
            verbose (bool, optional): if True, writes change to console. Defaults to False.
        """
        if verbose:
            print(f"Changing scenario from {cls.scenario} to {scenario}")
        
        cls.scenario = scenario
        cls.fp_data = os.path.join("data", cls.scenario, "data.csv")
    
    @classmethod
    def read_config(cls, fp_config: str):
        """Read configuration from a file

        Args:
            fp_config (str): filepath of config file. Right now this expects a csv with two columns [key, value]
        """
        df = pd.read_csv(fp_config)
        
        df_dict = df.set_index("key").to_dict()

        cls.setting1 = df_dict["setting1"]
        cls.setting2 = df_dict["setting2"]
        cls.setting3 = df_dict["setting3"]
        
        


    
