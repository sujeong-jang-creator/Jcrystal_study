ALTER SESSION SET STATISTICS_LEVEL = ALL; 

SELECT A.EMP_NO
     , A.EMP_NM
     , B.DEPT_CD
     , C.CERTI_CD 
  FROM TB_EMP A
     , TB_DEPT B
     , TB_EMP_CERTI C 
 WHERE B.DEPT_CD = '100004'
   AND A.DEPT_CD = A.DEPT_CD 
   AND A.EMP_NO = C.EMP_NO;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, 'ALLSTATS LAST')); 

SQL_ID  97u3brr83c21y, child number 1
-------------------------------------
SELECT A.EMP_NO      , A.EMP_NM      , B.DEPT_CD      , C.CERTI_CD    
FROM TB_EMP A      , TB_DEPT B      , TB_EMP_CERTI C   WHERE B.DEPT_CD 
= '100004'    AND A.DEPT_CD = A.DEPT_CD     AND A.EMP_NO = C.EMP_NO
 
Plan hash value: 1512580599
 
-------------------------------------------------------------------------------------------------------
| Id  | Operation                    | Name         | Starts | E-Rows | A-Rows |   A-Time   | Buffers |
-------------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |              |      1 |        |    123 |00:00:00.01 |     138 |
|   1 |  NESTED LOOPS                |              |      1 |    123 |    123 |00:00:00.01 |     138 |
|   2 |   NESTED LOOPS               |              |      1 |    123 |    123 |00:00:00.01 |      15 |
|   3 |    NESTED LOOPS              |              |      1 |    123 |    123 |00:00:00.01 |      10 |
|*  4 |     INDEX UNIQUE SCAN        | PK_TB_DEPT   |      1 |      1 |      1 |00:00:00.01 |       1 |
|   5 |     TABLE ACCESS FULL        | TB_EMP_CERTI |      1 |    123 |    123 |00:00:00.01 |       9 |
|*  6 |    INDEX UNIQUE SCAN         | PK_TB_EMP    |    123 |      1 |    123 |00:00:00.01 |       5 |
|   7 |   TABLE ACCESS BY INDEX ROWID| TB_EMP       |    123 |      1 |    123 |00:00:00.01 |     123 |
-------------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   4 - access("B"."DEPT_CD"='100004')
   6 - access("A"."EMP_NO"="C"."EMP_NO")
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2)
 
