
from unittest import case
from flask_restful import Resource
from util import parse_params
from flask_restful.reqparse import Argument
from flask import request
import subprocess

from repositories import ProvenancedRepository

class ProvenancedResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    def get(action):
        if action == "status":
            return ProvenancedRepository.getStatus()
        elif action == "netinfo":
            return ProvenancedRepository.getNetworkInfo()
        elif action == "keys":
            command = ["provenanced","keys","list","--home","../provenance/build/node0","--testnet"]
            result = subprocess.run(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines=True)
            return result.stdout.split("\n")
        elif action == "nhashHolders":
            command = ["provenanced","--testnet","q","marker","holding","nhash"]
            result = subprocess.run(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines=True)
            return result.stdout.split("\n")
            #provenanced --testnet q marker holding nhash
        else:
            return ""

    @staticmethod
    @parse_params(
        Argument("address", location="json", required=False, help="The address of the user.")
    )
    @parse_params(
        Argument("fromm", location="json", required=False, help="The address of the user.")
    )
    @parse_params(
        Argument("to", location="json", required=False, help="The address of the user.")
    )
    @parse_params(
        Argument("amount", location="json", required=False, help="The address of the user.")
    )
    def post(action,address,fromm,to,amount):
        try:
            if address == None:
                return "Address must be provided"
            if address[0:2] != "tp":
                    return "Expected tp, got something else"


            if action == "key":
                command = ["provenanced","keys","show","--testnet","--home","../provenance/build/node0",address]
                result = subprocess.run(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines=True)
                return result.stdout.split("\n")
            elif action == "balance":
                #provenanced --testnet q bank balances tp1zl388azlallp5rygath0kmpz6w2agpampukfc3
                command = ["provenanced","q","bank","balances",address,"--testnet","--home","../provenance/build/node0"]
                result = subprocess.run(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines=True)
                return result.stdout.split("\n")
            elif action == "mint":
                print("we are in mint")
                result = subprocess.check_output(["/root/flask-api-starter-kit/src/mint.sh",address])
                return {"to":address,"amount":"10 stableGBP","tx":str(result.splitlines()[2])}
            elif action == "transfer":
                print("we are in transfer")
                result = subprocess.check_output(["/root/flask-api-starter-kit/src/transfer.sh",address,address])
                return {"to":address,"amount":"5 stableGBP","tx":str(result.splitlines()[2])}
            elif action == "faucet":

                result = subprocess.check_output(["/root/flask-api-starter-kit/src/faucet.sh",address])
                return {"to":address,"amount":"10000","tx":str(result.splitlines()[2])}

        except Exception as e:
            print(e)
            raise f"An error happened, faucet action to wallet {address}"
        return ""

