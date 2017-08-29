codes = {
	"DRUG_CD": "약품코드",
	"DRUG_NM_ENG": "약품명(영문)",
	"DRUG_NM_KOR": "약품명(한글)",
	"INGRD_NM": "성분명",
	"INGRD_CD": "성분코드",
	"STR_YMD": "시작일자",
	"END_YMD": "종료일자",
	"HOSIO_ORD_GB" :"원내/원외 처방구분",
	"EFCY_CD": "효능코드(보건복지부)",
	"SUGA_CD": "수가코드",
	"EDI_CD": "EDI코드",
	"MNF_CO_CD": "제약회사코드",
	"MED_PTH": "투여경로",
	"MED_PTH_DTL": "상세투여경로",
	"USKD_CD": "제형코드",
	"IMP_DRUG_YN": "수입약품여부",
	"DRUG_MGT_GB": "약품관리구분",
	"CR_NO": "임상연구번호",
	"DRUG_LAW_GB": "약품법적구분",
	"ATBI_GB": "항균제구분",
	"ATCNC_GB": "항암제구분",
	"FDA_DIV_PRGNC": "FDA분류(임산부)",
	"FDA_DIV_SCKL": "FDA분류(수유부)",
	"SPLST_DRUG_YN": "전문의약품여부",
	"TRET_DRUG_YN": "처치약품여부",
	"TRET_DRUG_YN": "심평원평가구분",
	"PACK_UNIT": "포장단위",
	"STD_QTY": "규격량",
	"STD_UNIT": "규격단위",
	"CTN_QTY1": "함량1",
	"CTN_UNIT1": "함량단위1",
	"CTN_QTY2": "함량2",
	"CTN_UNIT2": "함량단위2",
	"CAP_QTY1": "용량1",
	"CAP_UNIT1": "용량단위1",
	"CAP_QTY2": "용량2",
	"CAP_UNIT2": "용량단위2",
	"HOSI_ORD_RESN_CD": "원내처방사유코드",
	"BAS_ORD_QTY_FRQ": "기본처방투여량(1회량)",
	"BAS_ORD_QTY_DAY": "기본처방투여량(1일량)",
	"BAS_ORD_UNIT_GB": "기본처방단위구분",
	"BAS_ORD_FRQ": "기본처방횟수",
	"BAS_ORD_DAY": "기본처방일수",
	"BAS_ORD_DSG_CD": "기본처방용법",
	"ORD_MAX_QTY_ADU": "처방최대량 (성인)",
	"ORD_MAX_QTY_CHD": "처방최대량 (소아)",
	"ORD_ALOW_YN_DEPT": "처방허용여부 (처방과별)",
	"ORD_ALOW_YN_DR": "처방허용여부 (처방의별)",
	"PRESC_FX_DSG_CD": "조제고정용법",
	"CAU_CD": "주의사항코드",
	"PWDR_PRESC_PSBL_YN": "산제가능여부",
	"TAB_SPLT_GB": "정제분할구분",
	"SNG_PACK_GB": "단일포장구분",
	"SLIP_PRT_EXCP_YN": "처방전 출력제외여부",
	"PRESC_CALC_STD_CD": "조제계산기준코드",
	"PRESC_STD_UNIT_GB": "조제기준단위구분",
	"PRESC_STD_UNIT": "조제기준단위",
	"SUGA_STD_UNIT_GB": "수가기준단위구분",
	"ACCU_DRUG_YN": "누적약품여부",
	"ACCU_DRUG_STD_QTY": "누적약품기준량",
	"ATC_PRESC_YN_O": "ATC조제여부(외래약국)",
	"ATC_PRESC_YN_I": "ATC조제여부(병실약국)",
	"DELV_DRUG_YN": "배달약품여부",
	"HDELV_PSBL_YN": "택배가능여부",
	"STOR_METH_CD": "보관방법코드",
	"SHD_STOR_YN": "차광보관여부",
	"ITEM_CD": "물품코드",
	"ITEM_REQ_CONV_QTY": "물품청구환산량",
	"DUSE_YN": "폐기여부",
	"DUSE_RESN_CD": "폐기사유코드",
	"DUSE_RESN_CONT": "폐기사유내용",
	"SUBS_YN": "대체여부",
	"SUBS_DRUG_CD": "대체약품코드",
	"PRN_YN": "PRN여부",
	"HIGH_ATTENTION": "고주의약품분류",
	"ORD_MAX_DAY": "처방최대일수",

}

columns = ["약품코드", "약품명(영문)", "약품명(한글)", "성분명", "시작일자", "종료일자", "원내/원외 처방구분", "보험단가", "일반단가", "효능코드(보건복지부)", "효능코드명", "기본처방용법명", "성분코드", "수가코드", "수가명", "EDI코드", "EDI단가", "제약회사코드", "제약회사명", "투여경로", "상세투여경로", "제형코드", "수입약품여부", "약품관리구분", "임상연구번호", "약품법적구분", "항균제구분", "항암제구분", "FDA분류(임산부)", "FDA분류(수유부)", "전문의약품여부", "처치약품여부", "심평원평가구분", "포장단위", "규격량", "규격단위", "함량1", "함량단위1", "함량2", "함량단위2", "용량1", "용량단위1", "용량2", "용량단위2", "원내처방사유코드", "기본처방투여량(1회량)", "기본처방투여량(1일량)", "기본처방단위구분", "기본처방횟수", "기본처방일수", "기본처방용법", "처방최대량 (성인)", "처방최대량 (소아)", "처방최대일수", "처방허용여부 (처방과별)", "처방허용여부 (처방의별)", "조제고정용법", "주의사항코드", "산제가능여부", "정제분할구분", "단일포장구분", "처방전 출력제외여부", "조제계산기준코드", "조제기준단위구분", "조제기준단위", "수가기준단위구분", "누적약품여부", "누적약품기준량", "ATC조제여부(외래약국)", "ATC조제여부(병실약국)", "배달약품여부", "택배가능여부", "보관방법코드", "보관용기코드", "차광보관여부", "감사대상여부", "복약상담대상여부", "물품코드", "물품명", "물품청구단위", "물품청구환산량", "비고(공개)", "비고(약국전용)", "약장위치", "대사효소", "대사기능에따른용량조절", "신청자ID", "신청일자", "신청일련번호", "수가확인여부", "수가확인자ID", "수가확인자명", "수가확인일시", "대체여부", "대체약품코드", "대체약품명", "폐기여부", "폐기사유코드", "폐기사유내용", "인슐린구분", "최대허용용량", "최대허용일수", "수가시작일자", "수가종료일자", "PRN여부", "고주의약품분류"]



























