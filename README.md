# LARGE SCALE DATA MANAGEMENT

## GROUP MEMBERS

- Yotlan LE CROM (<https://github.com/Yotlan>)
- Endy YU (<https://github.com/endyappel>)
- Florian MONSION (<https://github.com/JayCramboui>)

## PAGES RANK : PIG VS SPARK VS SPARK + CONTROLLED PARTITIONNING

With gs://public_lddm_data/page_links_en.nt.bz2 :

| Page Rank implementation  | Number of nodes  | Execution time (ms)  |
|---------------------------|------------------|----------------------|
| Pig                       | 1                | 5 965 137            |
| Pig                       | 2                | 2 926 194            |
| Pig                       | 4                | 2 097 353            |
| Pig                       | 5                | 1 936 174            |
| Spark                     | 1                | FAILED               |
| Spark                     | 2                | 2 457 349            |
| Spark                     | 4                | 1 755 194            |
| Spark                     | 5                | 1 777 790            |
| Spark + Controlled Part.  | 1                | FAILED               |
| Spark + Controlled Part.  | 2                | 1 507 807            |
| Spark + Controlled Part.  | 4                | 1 504 586            |
| Spark + Controlled Part.  | 5                | TODO                 |

With gs://public_lddm_data/small_page_links.nt :

| Page Rank implementation  | Number of nodes  | Execution time (ms)  |
|---------------------------|------------------|----------------------|
| Pig                       | 1                | TODO                 |
| Pig                       | 2                | TODO                 |
| Pig                       | 4                | TODO                 |
| Pig                       | 5                | TODO                 |
| Spark                     | 1                | TODO                 |
| Spark                     | 2                | TODO                 |
| Spark                     | 4                | TODO                 |
| Spark                     | 5                | TODO                 |
| Spark + Controlled Part.  | 1                | TODO                 |
| Spark + Controlled Part.  | 2                | TODO                 |
| Spark + Controlled Part.  | 4                | TODO                 |
| Spark + Controlled Part.  | 5                | TODO                 |