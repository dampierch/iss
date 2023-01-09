# To parse methylation classifier results
- A1) Consider whether subclass- or family-level result is relevant
- A2) Standardize result names so comparisons across classifiers can be made
- B1) Consider which combination of score results is present
- C1) Consider which results have most support (in terms of scores and classes)

## Score types
- 0.00-0.50 is LOW (L) and is discounted
- 0.50-0.85 is MEDIUM (M) and is suggestive
- 0.85-1.00 is HIGH (H) and is matching

## Combinations of score types
- Each of 3 variables can take 3 possible values, which gives 3^3 = 27
possible combinations
- see `base::expand.grid()` in R
```
expand.grid(c("H", "M", "L"), c("H", "M", "L"), c("H", "M", "L"))
```

### First set of combinations
- L L L :: inconclusive :: __INC__ module  
        "DNA methylation-based classification is inconclusive"  
        "results from (all) are non-contributory"
- L L M :: suggestive by nci :: __SUG by 1__ module  
        "there is no consensus methylation match but ..."  
        "... result from (highest) is suggestive of X"  
        "results from (lower 2) are non-contributory"
- L L H :: match by nci :: __MAT by 1__ module  
        "there is no consensus methylation match but ..."  
        "... result from (highest) is a high-confidence match to X"  
        "results from (lower 2) are non-contributory"
- L M L :: suggestive by v12 :: __SUG by 1__ module
- L M M :: suggestive by v12 and nci :: __SUG by 2__ module  
        :: must test whether same  
        "there is no consensus methylation match but ..."  
        if same then "... results from (highest 2) are suggestive of X"  
        if different, then sort by score  
        "... result from (higher) is suggestive of X while ..."  
        "... result from (lower) is suggestive of Y"  
        "result from (lowest) is non-contributory"
- L M H :: suggestive by v12 and match by nci :: __MAT by 1 SUG by 1__ module  
        :: must test whether same  
        "there is no consensus methylation match but ..."  
        if same, then  
        "... result from (higher) is a high-confidence match to X ..."  
        "... with suggestive support from (lower)"  
        if different, then  
        "... result from (higher) is a high-confidence match to X while ..."  
        "... result from (lower) is suggestive of Y"  
        "result from (lowest) is non-contributory"
- L H L :: match by v12 :: __MAT by 1__ module
- L H M :: match by v12 and suggestive by nci :: __MAT by 1 SUG by 1__ module
- L H H :: match by v12 and nci :: __MAT by 2__ module  
        :: must test whether same  
        "there is no consensus methylation match but ..."  
        if same, then  
        "... results from (highest 2) are high-confidence matches to X"  
        if different, then  
        "... result from (higher) is a high-confidence match to X while ..."  
        "... result from (lower) is a high-confidence match to Y"  
        "result from (lowest) is non-contributory"

### Second set of combinations
- M L L :: suggestive by v11 :: __SUG by 1__ module
- M L M :: suggestive by v11 and nci :: __SUG by 2__ module
- M L H :: suggestive by v11 and match by nci :: __MAT by 1 SUG by 1__ module
- M M L :: suggestive by v11 and v12 :: __SUG by 2__ module
- M M M :: suggestive by v11, v12, and nci :: __SUG by 3__ module  
        :: test whether same  
        "there is no consensus methylation match but ..."  
        if 3 are same, then  
        "... results from (all) are suggestive of X"  
        if 2 are same, then  
        "... results from (2 same) are suggestive of X while ..."  
        "... result from (other) is suggestive of Y"  
        if 3 are different, then  
        "... result from (highest) is suggestive of X, ..."  
        "... result from (next highest) is suggestive of Y, ..."  
        "... and result from (lowest) is suggestive of Z"
- M M H :: suggestive by v11 and v12 and match by nci :: __MAT by 1 SUG by 2__  
        :: test whether same  
        "there is no consensus methylation match but ..."  
        if 3 are same, then  
        "... result from (highest) is a high-confidence match to X with ..."  
        "... suggestive support from (lower 2)."  
        if 1 highest same as 1 other, then  
        "... result from (highest) is a high-confidence match to X ..."  
        "...with suggestive support from (1 same) while ..."  
        "... result from (1 different) is suggestive of Y"  
        if 1 highest different from other 2 but other 2 are same, then  
        "... result from (highest) is a high-confidence match to X ..."  
        "... while results from (lower 2) are suggestive of Y"  
        if 3 are different, then  
        "... result from (highest) is a high-confidence match to X ..."  
        "... while result from (higher of other 2) is suggestive of Y and ..."  
        "... result from (lower of other 2) is suggestive of Z"
- M H L :: suggestive by v11 and match by v12 :: __MAT by 1 SUG by 1__ module
- M H M :: suggestive by v11 and nci and match by v12 :: __MAT by 1 SUG by 2__
- M H H :: suggestive by v11 and match by v12 and nci :: __MAT by 2 SUG by 1__  
        :: test whether same  
        "there is no consensus methylation match but ..."  
        if 3 are same, then  
        "... results from (highest 2) are high-confidence matches to X with ..."  
        "... suggestive support from (lowest 1)."  
        if 2 highest are same but 1 lowest is different, then  
        "... results from (highest 2) are high-confidence matches to X while ..."  
        "... result from (lowest 1) is suggestive of Y"  
        if 1 lowest same as 1 of higher, then  
        "... result from (higher same as lowest) is a high-confidence match to X"  
        "... with suggestive support from (lowest same as higher) while ..."  
        "... (other higher) is a high-confidence match to Y"  
        if 3 are different, then  
        "... result from (highest) is a high-confidence match to X ..."  
        "... while result from (next highest) is a high-confidence match to Y"  
        "... and result from (lowest) is suggestive of Z"

### Third set of combinations
- H L L :: __MAT by 1__ module
- H L M :: __MAT by 1 SUG by 1__ module
- H L H :: __MAT by 2__ module
- H M L :: __MAT by 1 SUG by 1__ module
- H M M :: __MAT by 1 SUG by 2__ module
- H M H :: __MAT by 2 SUG by 1__ module
- H H L :: __MAT by 2__ module
- H H M :: __MAT by 2 SUG by 1__ module
- H H H :: __MAT by 3__ module  
        :: test whether same  
        if 3 are same, then  
        "there is a consensus methylation match to X."  
        "... results from (all) are high-confidence matches to X"  
        if 2 are same, then  
        "there is no consensus methylation match but ..."  
        "... results from (2 same) are high-confidence matches to X while ..."  
        "... result from (other) is high-confidence match to Y"  
        if 3 are different, then  
        "there is no consensus methylation match but ..."  
        "... result from (highest) is high-confidence match to X, ..."  
        "... result from (next highest) is high-confidence match to Y, ..."  
        "... and result from (lowest) is high-confidence match to Z"

## Modules required for parsing results
1. INC
2. SUG by 1
3. MAT by 1
4. SUG by 2
5. MAT by 1 SUG by 1
6. MAT by 2
7. SUG by 3
8. MAT by 1 SUG by 2
9. MAT by 2 SUG by 1
10. MAT by 3

## Missing classes
- If there are high-confidence or suggestive matches by one or two classifiers
to a class that does not exist in the other classifier(s), there could be a
"restricted" consensus.
- May require specification on a class-specific basis

## Important fields
- ID
- Sample
- Class1 :: DKFZ v11 subclass
- Class1.score
- MCF1 :: DKFZ v11 family
- MCF1.score
- CNSv12b6.subclass1
- CNSv12b6.subclass1.score
- Consistency_class :: NCI class
- Consistency_score
- Consistency_family :: NCI family
- Consistency_family_score
