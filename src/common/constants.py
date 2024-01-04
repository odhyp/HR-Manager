#----------# Webdriver Constants #----------#

# URLs
URL_SIMPEG = "https://simpeg2.jogjaprov.go.id/prod/"
URL_SIMPEG_NOMINATIF = f"{URL_SIMPEG}index.php/listing/nominatif"
URL_SIMPEG_DUK = f"{URL_SIMPEG}index.php/duk"
URL_PRESENSI = "https://presensi2.jogjaprov.go.id/"
URL_PRESENSI_REKAP_PRESENSI = f"{URL_PRESENSI}lap-pres/rekap/?menu_id=15"
URL_PRESENSI_REKAP_PRESTASI = f"{URL_PRESENSI}lap-pres/prestasi/?menu_id=16"

# Organization Name
NAMA_UNOR = "Kantor Pelayanan Pajak Daerah Daerah Istimewa Yogyakarta di Kabupaten Bantul"

# Time wait before next action (seconds)
# Mainly used in DriverSimpeg for working with dropdowns
WAIT_TIME = 3.5


#----------# PDF Constants #----------#

# Show cell borders (used for testing)
SHOW_BORDERS = False

# Page size (mm). Default is F4 paper
PAPER_SIZE = (215, 330)

# Page margins (mm). Top, bottom, left, and right margin
PAPER_MARGINS = 25.4

# Font size. Default is 12
FONT_SIZE = 12
