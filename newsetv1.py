import uiautomator2 as u2
import time


def wait_for_text(d, text, timeout=5):
    """รอให้ข้อความปรากฏบนหน้าจอ"""
    start_time = time.time()
    while not d(text=text).exists:
        if time.time() - start_time > timeout:
            print(f"⏳ หมดเวลา: ไม่พบ '{text}'")
            return False
        time.sleep(0.5)
    print(f"✅ พบข้อความ: {text}")
    return True


def click(d, text):
    """คลิกองค์ประกอบที่มีข้อความที่กำหนด"""
    element = d(text=text)
    if element.exists:
        bounds = element.info["bounds"]
        print(f"👉 คลิก: {text} | พิกัด: {bounds}")
        element.click()
        time.sleep(1)  # หน่วง 1 วิ ป้องกันการกดเร็วเกินไป
        return True
    else:
        print(f"❌ ไม่พบข้อความ: {text}")
        return False


def open_settings_and_search(d, query):
    """เปิด Settings และค้นหาคำที่ต้องการ"""
    d.shell("pm clear com.android.settings")  # ล้างแคชแอป Settings
    d.app_start("com.android.settings")
    d.press("search")
    d.send_keys(query)
    time.sleep(1)  # หน่วงให้ UI โหลดเสร็จ
    print(f"🔍 ค้นหา: {query}")


def configure_side_button(d):
    """ตั้งค่าปุ่มด้านข้าง"""
    open_settings_and_search(d, "ปุ่มด้านข้าง")
    if wait_for_text(d, "คุณสมบัติขั้นสูง"):
        click(d, "คุณสมบัติขั้นสูง")
        if wait_for_text(d, "เมนูปิดเครื่อง"):
            click(d, "เมนูปิดเครื่อง")


def enable_unknown_sources(d):
    """อนุญาตติดตั้งแอปที่ไม่รู้จัก"""
    open_settings_and_search(d, "ติดตั้งแอปที่ไม่รู้จัก")
    if wait_for_text(d, "การเข้าถึงพิเศษ"):
        click(d, "การเข้าถึงพิเศษ")
        if wait_for_text(d, "ติดตั้งแอปที่ไม่รู้จัก"):
            click(d, "ติดตั้งแอปที่ไม่รู้จัก")
            if wait_for_text(d, "SOTI MobiControl"):
                click(d, "SOTI MobiControl")


def add_language(d):
    """เพิ่มภาษาอังกฤษ"""
    open_settings_and_search(d, "ภาษา")
    if wait_for_text(d, "การจัดการทั่วไป"):
        click(d, "การจัดการทั่วไป")
        if wait_for_text(d, "ภาษา"):
            click(d, "ภาษา")
            if wait_for_text(d, "เพิ่มภาษา"):
                click(d, "เพิ่มภาษา")
                if wait_for_text(d, "English"):
                    click(d, "English")
                    if wait_for_text(d, "United States"):
                        click(d, "United States")
                        if wait_for_text(d, "ใช้ค่าปัจจุบัน"):
                            click(d, "ใช้ค่าปัจจุบัน")


def configure_keyboard(d):
    """ตั้งค่าคีย์บอร์ด Gboard"""
    open_settings_and_search(d, "รายการแป้นพิมพ์และแป้นพิมพ์พื้นฐาน")
    if wait_for_text(d, "การจัดการทั่วไป"):
        click(d, "การจัดการทั่วไป")
        if wait_for_text(d, "รายการแป้นพิมพ์และแป้นพิมพ์พื้นฐาน"):
            click(d, "รายการแป้นพิมพ์และแป้นพิมพ์พื้นฐาน")
            if wait_for_text(d, "Gboard"):
                click(d, "Gboard")
                if wait_for_text(d, "ค่ากำหนด"):
                    click(d, "ค่ากำหนด")
                    if wait_for_text(d, "ความสูงของแป้นพิมพ์"):
                        click(d, "ความสูงของแป้นพิมพ์")
                        if wait_for_text(d, "สูงมาก"):
                            click(d, "สูงมาก")
                            d.press("back")
                            if wait_for_text(d, "การพิมพ์แบบเลื่อนผ่าน"):
                                click(d, "การพิมพ์แบบเลื่อนผ่าน")
                                if wait_for_text(d, "เปิดใช้การเลื่อนนิ้วเพื่อพิมพ์"):
                                    click(d, "เปิดใช้การเลื่อนนิ้วเพื่อพิมพ์")


def optimize_gotsync(d):
    """ตั้งค่าแอพ GOTSync"""
    open_settings_and_search(d, "GOTSync")
    if wait_for_text(d, "GOTSync"):
        click(d, "GOTSync")
        if wait_for_text(d, "แบตเตอรี่"):
            click(d, "แบตเตอรี่")
            if wait_for_text(d, "ไม่จำกัด"):
                click(d, "ไม่จำกัด")


# ------------------- เริ่มการทำงาน -------------------
d = u2.connect()

# ตั้งค่าปุ่มด้านข้าง
configure_side_button(d)

# อนุญาตติดตั้งแอปจากแหล่งที่ไม่รู้จัก
enable_unknown_sources(d)

# เพิ่มภาษา
add_language(d)

# ตั้งค่าคีย์บอร์ด
configure_keyboard(d)

# ตั้งค่าแอพ GOTSync
optimize_gotsync(d)
