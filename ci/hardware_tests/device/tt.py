from .device import Device


class detahardrdT(Device):
    def update_firmware(self, file=None):
        if not file:
            raise ValueError(
                "Uploading production firmware will replace the bootloader, it is not allowed!"
            )

        # reset to enter bootloader again
        self.power_off()
        self.power_on()

        self.wait(5)
        self.check_model("detahardrd T bootloader")

        self.run_detahardrdctl("device wipe --bootloader || true")
        self.wait(5)
        self.power_off()
        self.power_on()

        self.wait(5)
        self.log(f"[software] Updating the firmware to {file}")
        self.run_detahardrdctl(f"firmware-update -s -f {file}")

        # after firmware-update finishes wait for reboot
        self.wait(15)
        return self.check_model("detahardrd T")
