//
//  main.cpp
//  January Challenge 2017 - Cats and Dogs
//
//  Created by S M HEMEL on 1/7/17.
//  Copyright © 2017 S M HEMEL. All rights reserved.
//

#include <stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        long long int c,d,l,min;
        scanf ("%lld %lld %lld",&c,&d,&l);
        if(2*d>=c)
            min=4*d;
        else if (2*d<c)
            min = 4*(c-d);
        
        if (l<min)
            printf("no\n");
        else if (l%4!=0)
            printf ("no\n");
        else if (l>= min && l<=4*(d+c) && l%4==0)
            printf ("yes\n");
        else
            printf ("no\n");
        
    }
    return 0;
}








