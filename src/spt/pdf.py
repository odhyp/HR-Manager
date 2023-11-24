from fpdf import FPDF

PAPER_SIZE_F4 = (215, 330)
BORDER_TEST = False


class PDF(FPDF):
    def header(self):
        self.set_y(1)
        self.set_font(family="times", style="B", size=12)
        self.cell(10, 5, "B", border=BORDER_TEST, align="R", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 40, border=BORDER_TEST, new_x="LMARGIN", new_y="NEXT")

    def chapter_title(self):
        self.set_font("times", "BU", 12)
        self.cell(0, 10, "SURAT PERINTAH TUGAS", border=BORDER_TEST, align="C", new_x="LMARGIN", new_y="NEXT")

        self.set_font("times", "", 12)
        self.cell(0, 2, "NOMOR : 800 / 1234", border=BORDER_TEST, align="C", new_x="LMARGIN", new_y="NEXT")

        self.ln(15)

    def chapter_body(self):
        self.set_font("Times", size=12)

        # Yang bertanda tangan
        self.multi_cell(0, 8,
                        "Yang bertanda tangan di bawah ini Kepala Kantor Pelayanan Pajak Daerah DIY di Kabupaten Bantul BPKA DIY, dengan ini memerintahkan kepada:",
                        new_x="LMARGIN", new_y="NEXT", border=BORDER_TEST)
        self.ln(5)

        # Data ASN
        # self.multi_cell(50, 8, "Nama\nNIP\nPangkat/Golongan\nJabatan\n", border=BORDER_TEST, new_x="RIGHT", new_y="LAST")

        asn_name = ['Nama',
                    'NIP',
                    'Pangkat/Golongan',
                    'Jabatan',
                    ]

        asn_value = ['ODHY PRADHANA, A.Md.Ak.',
                     '199904192021021002',
                     'Pengatur, II/c',
                     'Pengelola Gaji',
                     ]

        for i in range(len(asn_name)):
            self.multi_cell(20, 8, "", border=BORDER_TEST, new_x="RIGHT", new_y="LAST")
            self.multi_cell(40, 8, asn_name[i], border=BORDER_TEST, new_x="RIGHT", new_y="LAST")
            self.multi_cell(5, 8, ":", border=BORDER_TEST, new_x="RIGHT", new_y="LAST")
            self.multi_cell(0, 8, asn_value[i], border=BORDER_TEST, new_x="RIGHT", new_y="NEXT")
            self.ln(1)

        self.ln(5)

        data_name = ['Untuk',
                     'Hari/tanggal',
                     'Tujuan Tugas'
                     ]

        data_value = ['Rekonsiliasi Data dan Evaluasi Pendapatan Daerah Bulan Oktober Tahun 2023',
                      'Rabu, 8 November 2023',
                      'Badan Pengelola Keuangan dan Aset DIY']

        for i in range(len(data_name)):
            self.multi_cell(30, 8, data_name[i], border=BORDER_TEST, new_x="RIGHT", new_y="LAST")
            self.multi_cell(5, 8, ":", border=BORDER_TEST, new_x="RIGHT", new_y="LAST")
            self.multi_cell(0, 8, data_value[i], border=BORDER_TEST, new_x="RIGHT", new_y="NEXT")
            self.ln(1)

        self.ln(15)

        tanggal_value = '04 November 2023'

        tanggal_name = ['Dikeluarkan di Bantul',
                        'Pada tanggal : ' + tanggal_value,
                        ]

        for i in range(len(tanggal_name)):
            self.cell(60, 8, border=BORDER_TEST, new_x="RIGHT", new_y="LAST")
            self.cell(0, 8, tanggal_name[i], border=BORDER_TEST, new_x="RIGHT", new_y="NEXT")
            self.ln(1)

        self.set_font('times', 'B')
        self.cell(60, 8, border=BORDER_TEST, new_x="RIGHT", new_y="LAST")
        self.cell(0, 8, 'Plt. Kepala', align='C', border=BORDER_TEST, new_x="RIGHT", new_y="NEXT")
        self.ln(1)

        self.cell(0, 8 * 3, border=BORDER_TEST, new_x="RIGHT", new_y="NEXT")
        self.ln(1)

        kepala_name = ['HIDAYATI YULIASTANTRI DJOHAR, S.Sos., M.Si.',
                       'NIP. 19780723 200501 2 003']

        self.set_font('times', '')
        for i in range(len(kepala_name)):
            self.cell(60, 8, border=BORDER_TEST, new_x="RIGHT", new_y="LAST")
            self.cell(0, 8, kepala_name[i], align='C', border=BORDER_TEST, new_x="RIGHT", new_y="NEXT")
            self.ln(1)

    def print_chapter(self):
        self.add_page()

        # All margins are 2,54cm
        self.set_margin(25.4)

        self.chapter_title()
        self.chapter_body()
