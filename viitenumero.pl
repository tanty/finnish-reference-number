#!/usr/bin/perl

# viitenumero.pl
#
# (c) 2021 Alberto Garcia <berto@debian.org>
#
# This program calculates the Finnish reference number from a given
# natural number and returns it with the resulting ref. number and
# proper formatting.
#
# https://wiki.xmldation.com/support/fk/finnish_reference_number
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# http://www.gnu.org/licenses/gpl2.txt

use strict;
use warnings;
use bignum;

$ENV{LC_ALL} = "C";

$#ARGV == 0 or die "Usage: viitenumero.pl <number>\n";
($ARGV[0] =~ /^\d+$/) or die "Not a natural number $ARGV[0]\n";

my $refno = gen_ref_number("$ARGV[0]");

print "$refno\n";

exit 0;

sub gen_ref_number {
    my $number = shift;
    my $sum = 0;
    my $i = 0;
    my @factors = (7, 3, 1);
    for (my $tmp = $number; $tmp > 0; $tmp = int($tmp / 10)) {
        $sum += ($tmp % 10) * $factors[$i];
        $i = ($i + 1) % 3;
    }
    $number .= ((10 - ($sum % 10)) % 10);
    my $result = "";
    while ($number =~ /^(\d+)(\d\d\d\d\d)$/) {
        $result = "$2 $result";
        $number = $1;
    }
    $result = "$number $result";
    $result =~ s/ *$//;
    return $result;
}
