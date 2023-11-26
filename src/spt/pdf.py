from fpdf import FPDF

PAPER_SIZE_F4 = (215, 330)
BORDER_TEST = False


class PDF(FPDF):
    def header(self):
        """Add a header for the PDF page. Add letter "B" to follow
        Correspondence Guideline and excludes letterhead.
        """
        self.set_y(1)
        self.set_font(family="times",
                      style="B",
                      size=12)
        self.cell(w=10,
                  h=5,
                  text="B",
                  align="R",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=BORDER_TEST)
        self.cell(w=0,
                  h=40,
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=BORDER_TEST)

    def section_title(self, letter_number):
        """Add title section. 'Surat Perintah Tugas', Letter number, and
        Office Head opening paragraph.
        """
        # Section: SURAT PERINTAH TUGAS
        self.set_font(family="times",
                      style="BU",
                      size=12)
        self.cell(w=0,
                  h=4,
                  text="SURAT PERINTAH TUGAS",
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=BORDER_TEST)

        # Section: Nomor Surat
        self.set_font(family="times",
                      size=12)
        self.cell(w=0,
                  h=8,
                  text=f"NOMOR : 800 / {letter_number}",
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=BORDER_TEST)

        # Section: Perintah Kepala Kantor
        self.ln(8)
        self.set_font(family="times",
                      size=12)
        self.multi_cell(w=0,
                        h=8,
                        text="Yang bertanda tangan di bawah ini Kepala Kantor Pelayanan Pajak Daerah DIY di Kabupaten Bantul BPKA DIY, dengan ini memerintahkan kepada:",
                        new_x="LMARGIN",
                        new_y="NEXT",
                        border=BORDER_TEST)
        self.ln(4)

    def section_employee(self):
        """Add employee data including Nama, NIP, Pangkat/Golongan, Jabatan.
        """
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

        for i in range(4):
            self.multi_cell(w=20,
                            h=6,
                            text="x",  # testing line
                            align="R",
                            new_x="RIGHT",
                            new_y="LAST",
                            border=BORDER_TEST)
            self.multi_cell(w=40,
                            h=6,
                            text=asn_name[i],
                            new_x="RIGHT",
                            new_y="LAST",
                            border=BORDER_TEST)
            self.multi_cell(w=5,
                            h=6,
                            text=":",
                            new_x="RIGHT",
                            new_y="LAST",
                            border=BORDER_TEST)
            self.multi_cell(w=0,
                            h=6,
                            text=asn_value[i],
                            new_x="RIGHT",
                            new_y="NEXT",
                            border=BORDER_TEST)
            self.ln(1)

        self.ln(4)

    def section_assignment(self):
        """Add assignment data including Untuk, Hari/Tanggal, Tujuan Tugas.
        """
        data_name = ['Untuk',
                     'Hari/tanggal',
                     'Tujuan Tugas',
                     ]

        data_value = ['Rekonsiliasi Data dan Evaluasi Pendapatan Daerah Bulan Oktober Tahun 2023',
                      'Rabu, 8 November 2023',
                      'Badan Pengelola Keuangan dan Aset DIY Badan Pengelola Keuangan dan Aset DIY Badan Pengelola Keuangan dan Aset DIY',
                      ]

        for i in range(3):
            self.multi_cell(w=30,
                            h=8,
                            text=data_name[i],
                            new_x="RIGHT",
                            new_y="LAST",
                            border=BORDER_TEST)
            self.multi_cell(w=5,
                            h=8,
                            text=":",
                            new_x="RIGHT",
                            new_y="LAST",
                            border=BORDER_TEST)
            self.multi_cell(w=0,
                            h=8,
                            text=data_value[i],
                            new_x="RIGHT",
                            new_y="NEXT",
                            border=BORDER_TEST)
            self.ln(1)

        self.ln(8)

    def section_date(self):
        """Add letter date.
        """
        tanggal_name = ['Dikeluarkan di Bantul',
                        'Pada tanggal : ' + '26 November 2023',
                        ]

        for i in range(2):
            self.cell(w=60,
                      h=8,
                      new_x="RIGHT",
                      new_y="LAST",
                      border=BORDER_TEST)
            self.cell(w=0,
                      h=8,
                      text=tanggal_name[i],
                      new_x="RIGHT",
                      new_y="NEXT",
                      border=BORDER_TEST)
            self.ln(1)

    def section_signature(self):
        """Add Head office status, signature area, Head office name, Head
        office NIP.
        """
        self.set_font(family='times',
                      style='B',
                      size=12)
        self.cell(w=60,
                  h=8,
                  new_x="RIGHT",
                  new_y="LAST",
                  border=BORDER_TEST)
        self.cell(w=0,
                  h=8,
                  text='Plt. Kepala',
                  align='C',
                  new_x="RIGHT",
                  new_y="NEXT",
                  border=BORDER_TEST)

        self.ln(24)

        kepala_name = ['HIDAYATI YULIASTANTRI DJOHAR, S.Sos., M.Si.',
                       'NIP. 19780723 200501 2 003']

        self.set_font(family='times',
                      size=12)

        for i in range(2):
            self.cell(w=60,
                      h=4,
                      new_x="RIGHT",
                      new_y="LAST",
                      border=BORDER_TEST)
            self.cell(w=0,
                      h=4,
                      text=kepala_name[i],
                      align='C',
                      new_x="RIGHT",
                      new_y="NEXT",
                      border=BORDER_TEST)
            self.ln(1)

    def print_section(self):
        self.add_page()

        # All margins are 2,54cm
        self.set_margin(25.4)

        self.section_title(5670)
        self.section_employee()
        self.section_employee()
        self.section_employee()
        self.section_assignment()
        self.section_date()
        self.section_signature()
