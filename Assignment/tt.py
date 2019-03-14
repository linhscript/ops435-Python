
text = "Daily Usage Report for "
print(text+str(subject))
print(len(text+str(subject))*'=')
print("{:<14s}{:>14s}".format("Date","Usage in Seconds"))


if args.list:
    return text.append(str(args.list).tilte() + " list for " + str(args.filename))

elif args.type:
    return text.append(str(args.type).tilte() + " Usage Report for " + str(args.filename))

User list for usage_data_file
=============================

Host list for usage_data_file
=============================

Daily Usage Report for 10.40.105.130
====================================
Date          Usage in Seconds

Weekly Usage Report for rchan
=============================
Week #        Usage in Seconds

Monthly Usage Report for rchan
==============================
Month         Usage in Seconds