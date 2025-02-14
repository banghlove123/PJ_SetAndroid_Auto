import uiautomator2 as u2
import time


class Robot:
    def __init__(self):
        self.d = u2.connect()
        print("📲 Connected to device")
        self.d.shell("settings put system accelerometer_rotation 0")
        self.d.shell("settings put secure system locales th_TH")
        self.d.shell("settings put system screen_brightness_mode 0")  # ตั้งค่าแนวตรง
        self.d.shell("settings put system screen_brightness 255")  # ความสว่าง
        self.d.shell("settings put system screen_off_timeout 1800000")  # เวลาพักหน้าจอ

    def wait_for_text(self, text, timeout=5):
        """รอให้ข้อความปรากฏบนหน้าจอ"""
        start_time = time.time()
        while not self.d(text=text).exists:
            if time.time() - start_time > timeout:
                print(f"⏳ หมดเวลา: ไม่พบ '{text}'")
                return False
            time.sleep(0.5)
        print(f"✅ พบข้อความ: {text}")
        return True

    def click(self, text):
        """คลิกองค์ประกอบที่มีข้อความที่กำหนด"""
        element = self.d(text=text)
        if element.exists:
            bounds = element.info["bounds"]
            print(f"👉 คลิก: {text} | พิกัด: {bounds}")
            element.click()
            time.sleep(1)
            return True
        else:
            print(f"❌ ไม่พบข้อความ: {text}")
            return False

    def open_settings_and_search(self, query):
        """เปิด Settings และค้นหาคำที่ต้องการ"""
        self.d.shell("pm clear com.android.settings")
        self.d.app_start("com.android.settings")
        self.d.press("search")
        self.d.send_keys(query)
        time.sleep(1)
        print(f"🔍 ค้นหา: {query}")

    def configure_side_button(self):
        self.open_settings_and_search("ปุ่มด้านข้าง")
        if self.wait_for_text("คุณสมบัติขั้นสูง"):
            self.click("คุณสมบัติขั้นสูง")
            if self.wait_for_text("เมนูปิดเครื่อง"):
                self.click("เมนูปิดเครื่อง")

    def enable_unknown_sources(self):
        self.open_settings_and_search("ติดตั้งแอปที่ไม่รู้จัก")
        if self.wait_for_text("การเข้าถึงพิเศษ"):
            self.click("การเข้าถึงพิเศษ")
            if self.wait_for_text("ติดตั้งแอปที่ไม่รู้จัก"):
                self.click("ติดตั้งแอปที่ไม่รู้จัก")
                if self.wait_for_text("SOTI MobiControl"):
                    self.click("SOTI MobiControl")

    def add_language(self):
        self.open_settings_and_search("ภาษา")
        if self.wait_for_text("การจัดการทั่วไป"):
            self.click("การจัดการทั่วไป")
            if self.wait_for_text("ภาษา"):
                self.click("ภาษา")
                if self.wait_for_text("เพิ่มภาษา"):
                    self.click("เพิ่มภาษา")
                    if self.wait_for_text("English"):
                        self.click("English")
                        if self.wait_for_text("United States"):
                            self.click("United States")
                            if self.wait_for_text("ใช้ค่าปัจจุบัน"):
                                self.click("ใช้ค่าปัจจุบัน")

    def configure_keyboard(self):
        self.open_settings_and_search("รายการแป้นพิมพ์และแป้นพิมพ์พื้นฐาน")
        if self.wait_for_text("การจัดการทั่วไป"):
            self.click("การจัดการทั่วไป")
            if self.wait_for_text("รายการแป้นพิมพ์และแป้นพิมพ์พื้นฐาน"):
                self.click("รายการแป้นพิมพ์และแป้นพิมพ์พื้นฐาน")
                if self.wait_for_text("Gboard"):
                    self.click("Gboard")
                    if self.wait_for_text("ค่ากำหนด"):
                        self.click("ค่ากำหนด")
                        if self.wait_for_text("ความสูงของแป้นพิมพ์"):
                            self.click("ความสูงของแป้นพิมพ์")
                            if self.wait_for_text("สูงมาก"):
                                self.click("สูงมาก")
                                self.d.press("back")
                                if self.wait_for_text("การพิมพ์แบบเลื่อนผ่าน"):
                                    self.click("การพิมพ์แบบเลื่อนผ่าน")
                                    if self.wait_for_text("เปิดใช้การเลื่อนนิ้วเพื่อพิมพ์"):
                                        self.click("เปิดใช้การเลื่อนนิ้วเพื่อพิมพ์")

    def optimize_gotsync(self):
        self.open_settings_and_search("GOTSync1")
        if self.wait_for_text("GOTSync"):
            self.click("GOTSync")
            if self.wait_for_text("แบตเตอรี่"):
                self.click("แบตเตอรี่")
                if self.wait_for_text("ไม่จำกัด"):
                    self.click("ไม่จำกัด")

    def security(self):
        self.d.shell("adb shell")
        self.d.shell("locksettings set-pin 123456")  # ล็อค
        self.d.shell("am start -a android.settings.WIFI_SETTINGS")  # หน้า wifi
        self.d.shell("settings put system accelerometer_rotation 1")


if __name__ == "__main__":

    automation = Robot()
    automation.configure_side_button()
    automation.enable_unknown_sources()
    automation.add_language()
    automation.configure_keyboard()
    automation.optimize_gotsync()
    automation.security()
