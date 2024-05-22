#!/usr/bin/python3
"""UTF-8 Validation Module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""
    # Number of bytes remaining in the current UTF-8 character
    remaining_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Only consider the last 8 bits of the integer
        byte = byte & 0xFF

        if remaining_bytes == 0:
            # Determine how many bytes are in this UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 >> 1)) == (mask1 | mask2):
                # 2-byte character
                remaining_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 | mask2 | (mask2 >> 1)):
                # 3-byte character
                remaining_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 | mask2 | (mask2 >> 1)
                                                         | (mask2 >> 2)):
                # 4-byte character
                remaining_bytes = 3
            else:
                # Invalid UTF-8 character
                return False
        else:
            # Check continuation byte
            if (byte & (mask1 | mask2)) != mask1:
                return False
            remaining_bytes -= 1

    # If there are no remaining bytes, the UTF-8 encoding is valid
    return remaining_bytes == 0
