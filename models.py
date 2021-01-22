from exts import db

class GSM(db.Model):
    __tablename__ = 'gsm'
    id = db.Column(db.Integer, primary_key=True, comment='ID', autoincrement=True)
    GSM_num = db.Column(db.String(20), comment='GSM号')
    Status = db.Column(db.String(50), comment='发表时间')
    Source_name = db.Column(db.String(200), comment='器官类型')
    Organism = db.Column(db.String(100), comment='种属')
    Characteristics = db.Column(db.String(1000), comment='实验特征')
    Extracted_molecule = db.Column(db.String(100), comment='提取来源')
    Platform = db.Column(db.String(300), comment='平台')
    GSE_num = db.Column(db.String(20), db.ForeignKey('gse.GSE_num'), comment='GSE号')
    Experiment_type = db.Column(db.String(100), comment="实验类型")
    gse_en = db.relationship('GSE', backref=db.backref('gsms'))


class GSE(db.Model):
    __tablename__ = 'gse'
    id = db.Column(db.Integer, primary_key=True, comment='ID', autoincrement=True)
    GSE_num = db.Column(db.String(20), comment='GSE号', unique=True)
    Status = db.Column(db.String(50), comment='发表时间')
    Title = db.Column(db.String(300), comment='标题')
    Organism = db.Column(db.String(100), comment='种属')
    Experiment_type = db.Column(db.String(100), comment="实验类型")
    Summary = db.Column(db.Text, comment="摘要")
    Overall_design = db.Column(db.Text, comment="实验设计")
    Platforms = db.Column(db.Text, comment="平台")
    Samples = db.Column(db.Text, comment="GSM")
