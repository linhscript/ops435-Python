
# text = "Daily Usage Report for "
# print(text+str(subject))
# print(len(text+str(subject))*'=')
# print("{:<14s}{:>14s}".format("Date","Usage in Seconds"))

# def header:
# 	pass
# 	if args.list:
# 	    text.append(str(args.list).tilte() + " list for " + str(args.filename))

# 	elif args.type:
# 	    text.append(str(args.type).tilte() + " Usage Report for " + str(args.subject))
# 	    text.append()
def footer(records,total):
	ft = []
	for key in sorted(records.keys(),reverse=True):
		ft.append("{:<11s}{:>11d}".format(str(key),records[key]))
	ft.append("{:<11s}{:>11d}".format("Total",total))

print(footer)
# User list for usage_data_file
# =============================

# Host list for usage_data_file
# =============================

# Daily Usage Report for 10.40.105.130
# ====================================
# Date          Usage in Seconds

# Weekly Usage Report for rchan
# =============================
# Week #        Usage in Seconds

# Monthly Usage Report for rchan
# ==============================
# Month         Usage in Seconds

# for key in sorted(monthly_usage.keys(),reverse=True):
#     print ("{:<11s}{:>11d}".format(str(key),monthly_usage[key]))
# print("{:<11s}{:>11d}".format("Total",total))