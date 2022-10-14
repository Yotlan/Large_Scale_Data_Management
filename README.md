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
| Spark + Controlled Part.  | 5                | 1 469 502            |

The plot for this amount of data is bellow :

![page_links_en.nt.bz2 plot](img/page_links_en.nt.bz2.png)

With gs://public_lddm_data/small_page_links.nt :

| Page Rank implementation  | Number of nodes  | Execution time (ms)  |
|---------------------------|------------------|----------------------|
| Pig                       | 1                | 181 134              |
| Pig                       | 2                | 164 404              |
| Pig                       | 4                | 170 397              |
| Pig                       | 5                | TODO                 |
| Spark                     | 1                | 16 176               |
| Spark                     | 2                | 9 570                |
| Spark                     | 4                | 9 431                |
| Spark                     | 5                | TODO                 |
| Spark + Controlled Part.  | 1                | 13 535               |
| Spark + Controlled Part.  | 2                | 8 173                |
| Spark + Controlled Part.  | 4                | 8 591                |
| Spark + Controlled Part.  | 5                | TODO                 |

The plot for this amount of data is bellow :

![small_page_links.nt plot](img/small_page_links.nt.png)