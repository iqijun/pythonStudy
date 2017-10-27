# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Index, Integer, String, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class BizAugment(Base):
    __tablename__ = 'biz_augment'

    id = Column(BigInteger, primary_key=True)
    type = Column(Integer)
    s_subject_id = Column(BigInteger)
    chapter_id = Column(BigInteger)
    kp_id = Column(BigInteger)
    ext_params = Column(String(500))
    last_time = Column(DateTime)


class BizChoicetype(Base):
    __tablename__ = 'biz_choicetype'

    id = Column(BigInteger, primary_key=True)
    show_name = Column(String(100))
    name = Column(String(100))
    sub_obj_type = Column(Integer)
    answer_strategy = Column(String(50))
    description = Column(String(200))
    sort = Column(Integer)
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)


class BizChoicetypeSubjectLink(Base):
    __tablename__ = 'biz_choicetype_subject_link'

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    subject_id = Column(BigInteger, index=True)
    choicetype_id = Column(BigInteger)
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    points_strategy = Column(String(50), nullable=False)
    update_date = Column(DateTime, nullable=False)


class BizComputerTest(Base):
    __tablename__ = 'biz_computer_test'

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    s_subject_id = Column(BigInteger, index=True)
    name = Column(String(50))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(Integer)
    create_by = Column(String(64))
    create_date = Column(DateTime)
    update_by = Column(String(64))
    update_date = Column(DateTime)


class BizComputerTestPaperLink(Base):
    __tablename__ = 'biz_computer_test_paper_link'
    __table_args__ = (
        Index('index_computerId_deleteStatus', 'computer_test_id', 'delete_status'),
    )

    id = Column(BigInteger, primary_key=True)
    computer_test_id = Column(BigInteger)
    paper_id = Column(BigInteger)
    paper_use_type = Column(Integer)
    paper_sort = Column(Integer)
    delete_status = Column(Integer)
    create_by = Column(String(64))
    create_date = Column(DateTime)
    update_by = Column(String(64))
    update_date = Column(DateTime)


class BizExamRecordStatistic(Base):
    __tablename__ = 'biz_exam_record_statistics'

    id = Column(BigInteger, primary_key=True)
    channel_id = Column(BigInteger)
    member_id = Column(BigInteger)
    username = Column(String(64))
    paper_id = Column(BigInteger, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    query_status = Column(Integer)
    result_status = Column(Integer)
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime)


class BizMatch(Base):
    __tablename__ = 'biz_match'

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    s_subject_id = Column(BigInteger, index=True)
    paper_id = Column(BigInteger)
    name = Column(String(50))
    exam_model = Column(Integer)
    description = Column(Text)
    match_award_desc = Column(Text)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    analysis_open_time = Column(DateTime)
    done_flag = Column(Integer, server_default=text("'0'"))
    delete_status = Column(Integer, server_default=text("'0'"))
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)


class BizMatchPaperAnalysi(Base):
    __tablename__ = 'biz_match_paper_analysis'

    id = Column(BigInteger, primary_key=True)
    match_id = Column(BigInteger, index=True)
    member_num = Column(Integer)
    average_score = Column(Float(11))
    passing_score = Column(Float(11))
    pass_percent = Column(Float(5))


class BizMatchQuestionAnalysi(Base):
    __tablename__ = 'biz_match_question_analysis'
    __table_args__ = (
        Index('index_matchId_questionId', 'match_id', 'question_id'),
    )

    id = Column(BigInteger, primary_key=True)
    match_id = Column(BigInteger)
    question_id = Column(BigInteger)
    member_num = Column(Integer)
    error_percent = Column(Float(5))
    answer_distribution = Column(String(500))


class BizMatchTranscript(Base):
    __tablename__ = 'biz_match_transcript'
    __table_args__ = (
        Index('index_matchId_memberId', 'match_id', 'member_id'),
    )

    id = Column(BigInteger, primary_key=True)
    match_id = Column(BigInteger)
    member_id = Column(BigInteger)
    exam_record_id = Column(BigInteger)
    score = Column(Float(11))
    score_sort = Column(Integer)
    comment = Column(String(1000))
    comment_status = Column(Integer, server_default=text("'0'"))
    comment_by = Column(String(64))
    comment_time = Column(DateTime)


class BizMemberCollect(Base):
    __tablename__ = 'biz_member_collect'
    __table_args__ = (
        Index('index_memberId_subjectId_createTime', 'member_id', 'subject_id', 'create_time'),
    )

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    subject_id = Column(BigInteger)
    s_subject_id = Column(BigInteger)
    question_id = Column(BigInteger)
    choicetype_id = Column(BigInteger)
    create_time = Column(BigInteger)
    platform_code = Column(Integer)


class BizMemberError(Base):
    __tablename__ = 'biz_member_error'
    __table_args__ = (
        Index('index_memberId_subjectId_updateTime', 'member_id', 'subject_id', 'update_time'),
    )

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    subject_id = Column(BigInteger)
    s_subject_id = Column(BigInteger)
    question_id = Column(BigInteger)
    choicetype_id = Column(BigInteger)
    count = Column(Integer)
    create_time = Column(BigInteger)
    update_time = Column(BigInteger)
    platform_code = Column(Integer)


class BizMemberExamDetail(Base):
    __tablename__ = 'biz_member_exam_detail'

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger, index=True)
    exam_record_id = Column(BigInteger, index=True)
    choicetype_id = Column(BigInteger)
    paper_section_id = Column(BigInteger)
    question_id = Column(BigInteger)
    is_group = Column(Integer)
    group_id = Column(BigInteger)
    score = Column(Float(11))
    my_answer = Column(Text)
    is_right = Column(Integer)
    create_time = Column(BigInteger)
    waste_time = Column(BigInteger)


class BizMemberExamKpTop(Base):
    __tablename__ = 'biz_member_exam_kp_top'
    __table_args__ = (
        Index('index_sSubjectId_totalType_status', 's_subject_id', 'total_type', 'status'),
    )

    id = Column(BigInteger, primary_key=True)
    s_subject_id = Column(BigInteger)
    kp_id = Column(BigInteger)
    kp_name = Column(String(200))
    count = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    total_type = Column(Integer)
    status = Column(Integer)


class BizMemberExamRecord(Base):
    __tablename__ = 'biz_member_exam_record'
    __table_args__ = (
        Index('index_status_endTime', 'status', 'end_time'),
        Index('index_examModel_status_startTime', 'exam_model', 'status', 'start_time'),
        Index('index_sSubjectId_platformCode_memberId_examModel', 's_subject_id', 'platform_code', 'member_id', 'exam_model')
    )

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    subject_id = Column(BigInteger)
    s_subject_id = Column(BigInteger)
    paper_id = Column(BigInteger)
    paper_name = Column(String(100))
    papertype_id = Column(BigInteger)
    totle_num = Column(Integer)
    answer_num = Column(Integer)
    total_score = Column(Float(11))
    right_num = Column(Integer)
    score = Column(Float(11))
    start_time = Column(BigInteger)
    time_cost = Column(BigInteger)
    end_time = Column(BigInteger)
    exam_model = Column(Integer)
    match_id = Column(BigInteger)
    commit_type = Column(Integer)
    status = Column(Integer)
    platform_code = Column(Integer)


class BizMemberExamSection(Base):
    __tablename__ = 'biz_member_exam_section'

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    exam_record_id = Column(BigInteger, index=True)
    choicetype_id = Column(BigInteger)
    paper_section_id = Column(BigInteger)
    totle_num = Column(Integer)
    total_score = Column(Float(11))
    right_num = Column(Integer)
    score = Column(Float(11))


class BizMemberTkNote(Base):
    __tablename__ = 'biz_member_tk_note'
    __table_args__ = (
        Index('index_memberId_subjectId', 'member_id', 'subject_id'),
    )

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    subject_id = Column(BigInteger)
    s_subject_id = Column(BigInteger)
    chapter_id = Column(BigInteger)
    question_id = Column(BigInteger)
    choicetype_id = Column(BigInteger)
    title = Column(String(100))
    content = Column(String(1200))
    create_time = Column(BigInteger)
    update_time = Column(BigInteger)
    platform_code = Column(Integer)


class BizNoteImgLink(Base):
    __tablename__ = 'biz_note_img_link'

    id = Column(BigInteger, primary_key=True)
    note_id = Column(BigInteger)
    img_url = Column(String(256))


class BizPaper(Base):
    __tablename__ = 'biz_paper'
    __table_args__ = (
        Index('index_sSubjectId_papertypeId_publishStatus', 's_subject_id', 'papertype_id', 'publish_status'),
    )

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    s_subject_id = Column(BigInteger)
    source = Column(Integer)
    difficulty_level = Column(Integer)
    name = Column(String(100))
    papertype_id = Column(BigInteger)
    effective_date = Column(DateTime)
    limited_time = Column(Integer)
    total_score = Column(Float(5))
    passing_score = Column(Float(5))
    determinant = Column(Integer)
    moment = Column(Integer, server_default=text("'1'"))
    can_download = Column(Integer)
    download_url = Column(String(200))
    status = Column(Integer, server_default=text("'1'"))
    delete_status = Column(Integer, index=True)
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)
    publish_status = Column(Integer, server_default=text("'0'"))
    publisher = Column(String(64))
    publish_date = Column(DateTime)
    qr_code_num = Column(BigInteger, index=True)
    is_free = Column(Integer)
    sort = Column(Integer)


class BizPaperChoicetypeLink(Base):
    __tablename__ = 'biz_paper_choicetype_link'

    id = Column(BigInteger, primary_key=True)
    paper_id = Column(BigInteger, index=True)
    choicetype_id = Column(BigInteger)
    name = Column(String(100))
    score = Column(Float(5))
    question_count = Column(Integer)
    sort = Column(Integer)
    description = Column(String(200))


class BizPaperQuestionLink(Base):
    __tablename__ = 'biz_paper_question_link'

    id = Column(BigInteger, primary_key=True)
    paper_id = Column(BigInteger, index=True)
    paper_choice_type_id = Column(BigInteger)
    question_id = Column(BigInteger)
    is_group = Column(Integer, server_default=text("'0'"))
    group_id = Column(BigInteger)
    sort = Column(Integer)
    score = Column(Float(5))


class BizPaperTagLink(Base):
    __tablename__ = 'biz_paper_tag_link'
    __table_args__ = (
        Index('index_tagId_paperId', 'tag_id', 'paper_id'),
    )

    id = Column(BigInteger, primary_key=True)
    paper_id = Column(BigInteger)
    tag_id = Column(BigInteger)


class BizPapertype(Base):
    __tablename__ = 'biz_papertype'

    id = Column(BigInteger, primary_key=True)
    show_name = Column(String(100))
    name = Column(String(100))
    type = Column(Integer, server_default=text("'0'"))
    icon = Column(String(255))
    sort = Column(Integer)
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)
    description = Column(String(200))


class BizPapertypeSeasonLink(Base):
    __tablename__ = 'biz_papertype_season_link'

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    s_subject_id = Column(BigInteger, index=True)
    papertype_id = Column(BigInteger)
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)
    platform = Column(Integer, server_default=text("'0'"))


class BizPlatformPapertypeLink(Base):
    __tablename__ = 'biz_platform_papertype_link'
    __table_args__ = (
        Index('index_sSubjectId_platformCode', 's_subject_id', 'platform_code'),
    )

    id = Column(BigInteger, primary_key=True)
    platform_code = Column(Integer)
    exam_id = Column(BigInteger)
    s_subject_id = Column(BigInteger)
    paper_type_id = Column(BigInteger)
    status = Column(Integer)
    create_by = Column(String(64))
    create_date = Column(DateTime)
    update_by = Column(String(64))
    update_date = Column(DateTime)


class BizPrivatePracticeRule(Base):
    __tablename__ = 'biz_private_practice_rules'

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    s_subject_id = Column(BigInteger)
    name = Column(String(50))
    status = Column(Integer)
    update_by = Column(String(64))
    update_date = Column(DateTime)
    create_by = Column(String(64))
    create_date = Column(DateTime)


class BizPrivatePracticeRulesDetail(Base):
    __tablename__ = 'biz_private_practice_rules_detail'

    id = Column(BigInteger, primary_key=True)
    rules_id = Column(BigInteger)
    classify_id = Column(String(200))
    choice_type = Column(BigInteger)
    difficulty_level = Column(Integer)
    question_num = Column(Integer)
    description = Column(String(200))
    sort = Column(Integer)
    update_by = Column(String(64))
    update_date = Column(DateTime)
    create_by = Column(String(64))
    create_date = Column(DateTime)


class BizProgres(Base):
    __tablename__ = 'biz_progress'

    id = Column(BigInteger, primary_key=True)
    type = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    execute_num = Column(Integer)
    result = Column(Integer)
    des = Column(String(200))
    last_index = Column(BigInteger)


class BizQuestion(Base):
    __tablename__ = 'biz_question'
    __table_args__ = (
        Index('index_subjectId_choicetypeId', 'subject_id', 'choicetype_id'),
    )

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    subject_id = Column(BigInteger)
    is_group = Column(Integer, server_default=text("'0'"))
    group_id = Column(BigInteger, index=True)
    seq = Column(Integer)
    difficulty_level = Column(Integer)
    default_score_value = Column(Float(11))
    short_title = Column(String(255))
    title = Column(Text)
    choicetype_id = Column(BigInteger)
    right_answers = Column(Text)
    solutions = Column(String)
    analysis = Column(Text)
    cy_answer_type = Column(Integer)
    cy_subtopic_num = Column(Integer)
    cy_question_id = Column(String(64))
    cy_operation_video = Column(String(500))
    option_type = Column(Integer, server_default=text("'0'"))
    status = Column(Integer, server_default=text("'1'"))
    auditor = Column(String(64))
    audit_date = Column(DateTime)
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)


class BizQuestionClassify(Base):
    __tablename__ = 'biz_question_classify'

    id = Column(BigInteger, primary_key=True)
    code = Column(String(50))
    name = Column(String(50))
    sort = Column(Integer)
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)


class BizQuestionCy(Base):
    __tablename__ = 'biz_question_cy'

    id = Column(BigInteger, primary_key=True)
    question_id = Column(BigInteger, index=True)
    cy_answer_type = Column(Integer)
    cy_subtopic_num = Column(Integer)
    cy_question_id = Column(String(64))
    cy_operation_video = Column(String(500))


class BizQuestionDailyPractice(Base):
    __tablename__ = 'biz_question_daily_practice'

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    subject_id = Column(BigInteger)
    s_subject_id = Column(BigInteger)
    question_id = Column(BigInteger)


class BizQuestionErratum(Base):
    __tablename__ = 'biz_question_errata'
    __table_args__ = (
        Index('index_memberId_sSubjectId_questionId', 'member_id', 's_subject_id', 'question_id'),
    )

    id = Column(BigInteger, primary_key=True)
    question_id = Column(BigInteger, nullable=False)
    s_subject_id = Column(BigInteger)
    platform_code = Column(Integer)
    context = Column(String(500))
    status = Column(Integer, server_default=text("'1'"))
    member_id = Column(BigInteger, nullable=False)
    create_date = Column(DateTime, nullable=False)
    auditor = Column(String(64))
    auditor_date = Column(DateTime)


class BizQuestionErrataTypeLink(Base):
    __tablename__ = 'biz_question_errata_type_link'

    id = Column(BigInteger, primary_key=True)
    errata_id = Column(BigInteger, nullable=False, index=True)
    errata_type = Column(Integer, nullable=False)


class BizQuestionOption(Base):
    __tablename__ = 'biz_question_option'

    id = Column(BigInteger, primary_key=True)
    question_id = Column(BigInteger, index=True)
    tag = Column(String(50))
    description = Column(Text)
    sort = Column(Integer)


class BizQuestionSign(Base):
    __tablename__ = 'biz_question_sign'

    id = Column(BigInteger, primary_key=True)
    question_id = Column(BigInteger, index=True)
    sign = Column(String(500))


class BizSeasonQuestionBookLink(Base):
    __tablename__ = 'biz_season_question_book_link'
    __table_args__ = (
        Index('index_questionId_sSubjectId', 'question_id', 's_subject_id'),
    )

    id = Column(BigInteger, primary_key=True)
    s_subject_id = Column(BigInteger)
    book_id = Column(BigInteger)
    chapter_id = Column(BigInteger)
    question_id = Column(BigInteger)
    page_num = Column(Integer)
    question_num = Column(Integer)
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)


class BizSeasonQuestionClassifyLink(Base):
    __tablename__ = 'biz_season_question_classify_link'
    __table_args__ = (
        Index('index_questionId_sSubjectId', 'question_id', 's_subject_id'),
    )

    id = Column(BigInteger, primary_key=True)
    s_subject_id = Column(BigInteger)
    classify_id = Column(BigInteger)
    question_id = Column(BigInteger)
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)


class BizSeasonQuestionKpLink(Base):
    __tablename__ = 'biz_season_question_kp_link'
    __table_args__ = (
        Index('index_questionId_sSubjectId', 'question_id', 's_subject_id'),
    )

    id = Column(BigInteger, primary_key=True)
    s_subject_id = Column(BigInteger)
    question_id = Column(BigInteger)
    chapter_id = Column(BigInteger)
    kp_id = Column(BigInteger)
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)


class TemChoicetype(Base):
    __tablename__ = 'tem_choicetype'

    id = Column(BigInteger, primary_key=True)
    show_name = Column(String(100))
    name = Column(String(100))
    sub_obj_type = Column(Integer)
    answer_strategy = Column(String(50))
    description = Column(String(200))
    sort = Column(Integer)
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)


class TemPaper(Base):
    __tablename__ = 'tem_paper'
    __table_args__ = (
        Index('index_sSubjectId_papertypeId_publishStatus', 's_subject_id', 'papertype_id', 'publish_status'),
    )

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    s_subject_id = Column(BigInteger)
    source = Column(Integer)
    difficulty_level = Column(Integer)
    name = Column(String(100))
    papertype_id = Column(BigInteger)
    effective_date = Column(DateTime)
    limited_time = Column(Integer)
    total_score = Column(Float(5))
    passing_score = Column(Float(5))
    determinant = Column(Integer)
    moment = Column(Integer, server_default=text("'1'"))
    can_download = Column(Integer)
    download_url = Column(String(200))
    status = Column(Integer, server_default=text("'1'"))
    delete_status = Column(Integer, index=True)
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)
    publish_status = Column(Integer, server_default=text("'0'"))
    publisher = Column(String(64))
    publish_date = Column(DateTime)
    qr_code_num = Column(BigInteger, index=True)
    is_free = Column(Integer)
    sort = Column(Integer)


class TemPaperChoicetypeLink(Base):
    __tablename__ = 'tem_paper_choicetype_link'

    id = Column(BigInteger, primary_key=True)
    paper_id = Column(BigInteger, index=True)
    choicetype_id = Column(BigInteger)
    name = Column(String(100))
    score = Column(Float(5))
    question_count = Column(Integer)
    sort = Column(Integer)
    description = Column(String(200))


class TemPaperQuestionLink(Base):
    __tablename__ = 'tem_paper_question_link'

    id = Column(BigInteger, primary_key=True)
    paper_id = Column(BigInteger, index=True)
    paper_choice_type_id = Column(BigInteger)
    question_id = Column(BigInteger)
    is_group = Column(Integer, server_default=text("'0'"))
    group_id = Column(BigInteger)
    sort = Column(Integer)
    score = Column(Float(5))


class TemPapertype(Base):
    __tablename__ = 'tem_papertype'

    id = Column(BigInteger, primary_key=True)
    show_name = Column(String(100))
    name = Column(String(100))
    type = Column(Integer, server_default=text("'0'"))
    icon = Column(String(255))
    sort = Column(Integer)
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)
    description = Column(String(200))


class TemQuestion(Base):
    __tablename__ = 'tem_question'
    __table_args__ = (
        Index('index_subjectId_choicetypeId', 'subject_id', 'choicetype_id'),
    )

    id = Column(BigInteger, primary_key=True)
    exam_id = Column(BigInteger)
    subject_id = Column(BigInteger)
    is_group = Column(Integer, server_default=text("'0'"))
    group_id = Column(BigInteger, index=True)
    seq = Column(Integer)
    difficulty_level = Column(Integer)
    default_score_value = Column(Float(11))
    short_title = Column(String(255))
    title = Column(Text)
    choicetype_id = Column(BigInteger)
    right_answers = Column(Text)
    solutions = Column(String)
    analysis = Column(Text)
    cy_answer_type = Column(Integer)
    cy_subtopic_num = Column(Integer)
    cy_question_id = Column(String(64))
    cy_operation_video = Column(String(500))
    option_type = Column(Integer, server_default=text("'0'"))
    status = Column(Integer, server_default=text("'1'"))
    auditor = Column(String(64))
    audit_date = Column(DateTime)
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)


class TemQuestionOption(Base):
    __tablename__ = 'tem_question_option'

    id = Column(BigInteger, primary_key=True)
    question_id = Column(BigInteger, index=True)
    tag = Column(String(50))
    description = Column(Text)
    sort = Column(Integer)


class TemSeasonQuestionKpLink(Base):
    __tablename__ = 'tem_season_question_kp_link'
    __table_args__ = (
        Index('index_questionId_sSubjectId', 'question_id', 's_subject_id'),
    )

    id = Column(BigInteger, primary_key=True)
    s_subject_id = Column(BigInteger)
    question_id = Column(BigInteger)
    chapter_id = Column(BigInteger)
    kp_id = Column(BigInteger)
    status = Column(Integer, server_default=text("'1'"))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False)
    update_by = Column(String(64), nullable=False)
    update_date = Column(DateTime, nullable=False)
