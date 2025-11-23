### Test Case 1: CET to others
Command: python meeting_converter.py "2025-12-25" "10:00" "CET"
Output:
```
Original Time: 2025-12-25 10:00 CET+0100
----------------------------------------
EST  : 2025-12-25 04:00 EST-0500
IST  : 2025-12-25 14:30 IST+0530
UTC  : 2025-12-25 09:00 UTC+0000
```

### Test Case 2: UTC to others
Command: python meeting_converter.py "2025-01-01" "00:00" "UTC"
Output:
```
Original Time: 2023-01-01 00:00 UTC+0000
----------------------------------------
EST  : 2024-12-31 19:00 EST-0500
IST  : 2025-01-01 05:30 IST+0530
UTC  : 2025-01-01 00:00 UTC+0000
```

### Test Case 3: Flexible Input Support
Command: python meeting_converter.py "2023-12-25 10:00:00" "CET"
Output:
```
Original Time: 2025-12-25 10:00:00 CET+0100
----------------------------------------
EST  : 2025-12-25 04:00:00 EST-0500
IST  : 2025-12-25 14:30:00 IST+0530
UTC  : 2025-12-25 09:00:00 UTC+0000
```

