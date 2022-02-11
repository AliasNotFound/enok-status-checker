import os
import json

sample_output = "{\"buildPlate_target_temperature\":60,\"chamber_temperature\":26,\"door_open\":0,\"elaspedtime\":0,\"error_code\":200,\"extruder_target_temperature\":0,\"fanSpeed\":0,\"filament_type \":\"PLA\",\"firmware_version\":\"v3.0_R02.11.17\",\"jobname\":\"45-pla-sword-sheath.gcode\",\"jobstatus\":\"preparing\",\"layer\":0,\"message\":\"success\",\"networkBuild\":0,\"platform_temperature\":58,\"progress\":0,\"remaining\":0,\"status\":\"busy\",\"temperature\":40,\"totalTime\":0}"


class StatusManager:
    def __init__(self):
        config = open("config.json", "r")
        json_config = config.read()
        config.close()
        config = json.loads(json_config)
        self.config = config

    @staticmethod
    def get_printer_status(printer_ips):
        for item in printer_ips:
            if isinstance(item, str):
                # Formats curl command
                curl_cmd = "curl --location --request POST \'http://" + item + "/command\' --header \'Content-Type: application/x-www-form-urlencoded\' --data-urlencode \'GETPRINTERSTATUS=\'"
                # calls printer status and stores JSON call to string
                printer_status = os.popen(curl_cmd).read()
                printer_status = json.loads(printer_status)
                # printer_status = json.loads(sample_output)
                print(printer_status)
                return printer_status
